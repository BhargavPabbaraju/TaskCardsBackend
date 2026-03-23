"""Task item models."""

from enum import Enum

from sqlalchemy import Boolean
from sqlalchemy import Enum as SQLEnum
from sqlalchemy import ForeignKey, Integer, String, Text, event, func, select
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.extensions import db


class EnergyLevel(Enum):
    """Energy needed for a task."""

    NIL = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    HYPER = 4


class Topic(db.Model):
    """A topic under a domain, such as Caching or Sliding Window."""

    __tablename__ = "topics"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    domain_key: Mapped[str] = mapped_column(String(50), nullable=False)
    domain_sort_order: Mapped[int | None] = mapped_column(
        Integer, nullable=True, default=0
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    is_active: Mapped[bool] = mapped_column(nullable=False, default=True)

    task_items: Mapped[list["TaskItem"]] = relationship(
        back_populates="topic",
        cascade="all, delete-orphan",
    )

    def __str__(self) -> str:
        return f"{self.name} [{self.domain_key}]"


@event.listens_for(Topic, "before_insert")
def set_domain_sort_order(_, connection, target):
    """Auto-assign domain_sort_order within a domain."""
    if target.domain_key is None or target.domain_sort_order is not None:
        return

    topics = Topic.__table__

    max_order_query = select(func.max(topics.c.domain_sort_order)).where(
        topics.c.domain_key == target.domain_key
    )
    max_order = connection.execute(max_order_query).scalar()

    target.domain_sort_order = 0 if max_order is None else max_order + 1


class TaskItem(db.Model):
    """A task card that can be displayed to the user."""

    __tablename__ = "task_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    topic_sort_order: Mapped[int | None] = mapped_column(
        Integer, nullable=True, default=0
    )
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=True, default=True)
    min_energy: Mapped[EnergyLevel | None] = mapped_column(
        SQLEnum(EnergyLevel), nullable=True
    )
    est_mins: Mapped[int | None] = mapped_column(Integer, nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    topic_id: Mapped[str] = mapped_column(ForeignKey("topics.id"), nullable=False)
    topic: Mapped["Topic"] = relationship(back_populates="task_items")

    checklist_items: Mapped[list["TaskChecklistItem"]] = relationship(
        back_populates="task_item",
        cascade="all, delete-orphan",
        order_by="TaskChecklistItem.sort_order",
    )

    links: Mapped[list["TaskLink"]] = relationship(
        back_populates="task_item",
        cascade="all, delete-orphan",
        order_by="TaskLink.sort_order",
    )


@event.listens_for(TaskItem, "before_insert")
def set_topic_sort_order(_, connection, target):
    """Auto-assign topic_sort_order within a topic."""
    if target.topic_id is None or target.topic_sort_order is not None:
        return

    task_items = TaskItem.__table__

    max_order_query = select(func.max(task_items.c.topic_sort_order)).where(
        task_items.c.topic_id == target.topic_id
    )
    max_order = connection.execute(max_order_query).scalar()

    target.topic_sort_order = 0 if max_order is None else max_order + 1


class TaskChecklistItem(db.Model):
    """A checklist line belonging to a task item."""

    __tablename__ = "task_checklist_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    text: Mapped[str] = mapped_column(String(255), nullable=False)

    task_item_id: Mapped[int] = mapped_column(
        ForeignKey("task_items.id"), nullable=False
    )
    task_item: Mapped["TaskItem"] = relationship(back_populates="checklist_items")


class TaskLink(db.Model):
    """A link belonging to a task item."""

    __tablename__ = "task_links"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    label: Mapped[str] = mapped_column(String(255), nullable=False)
    url: Mapped[str] = mapped_column(Text, nullable=False)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    task_item_id: Mapped[int] = mapped_column(
        ForeignKey("task_items.id"), nullable=False
    )
    task_item: Mapped["TaskItem"] = relationship(back_populates="links")
