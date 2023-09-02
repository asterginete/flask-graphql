import graphene
from app.models import Notification as NotificationModel
from app import db
from app.schema.types import NotificationType

class CreateNotification(graphene.Mutation):
    class Arguments:
        user_id = graphene.Int(required=True)
        content = graphene.String(required=True)

    notification = graphene.Field(NotificationType)

    def mutate(root, info, user_id, content):
        notification = NotificationModel(user_id=user_id, content=content)
        db.session.add(notification)
        db.session.commit()
        return CreateNotification(notification=notification)

class UpdateNotification(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        content = graphene.String()

    notification = graphene.Field(NotificationType)

    def mutate(root, info, id, content=None):
        notification = db.session.query(NotificationModel).filter_by(id=id).first()
        if notification and content:
            notification.content = content
            db.session.commit()
        return UpdateNotification(notification=notification)

class DeleteNotification(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(root, info, id):
        notification = db.session.query(NotificationModel).filter_by(id=id).first()
        if notification:
            db.session.delete(notification)
            db.session.commit()
            return DeleteNotification(success=True)
        return DeleteNotification(success=False)
