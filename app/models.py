# Model is a representation of a table in a database (Important for later
# when we create the timeseries Stuff

from app import db

class BucketList(db.Model):

    __tablename__ = 'bucketlists'

    id = db.Columns(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.Datetime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp()
    )

    def __repr__(self):
        return 'BucketList %r' % self.name

    def __init__(self, name):
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return BucketList.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()