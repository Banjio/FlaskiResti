# Model is a representation of a table in a database (Important for later
# when we create the timeseries Stuff

from app import db

class BucketList(db.Model):

    __tablename__ = 'bucketlists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
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

    def get_dict_repr(self):
        return {
            'id': self.id,
            'name': self.name,
            'date_created': self.date_created,
            'date_modified': self.date_modified}

class GameSales(db.Model):

    __tablename__ = 'game_sales'
    name = db.Column(db.String(255), primary_key=True)
    platform = db.Column(db.String(255), primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp()
    )
    rank = db.Column(db.Integer)
    year = db.Column(db.Integer)
    genre = db.Column(db.String(255))
    publisher = db.Column(db.String(255))
    global_sales = db.Column(db.Float)

    def __repr__(self):
        return 'GameSales %r' % self.name

    def __init__(self, name, platform, rank, year, genre, publisher, global_sales):
        self.name = name
        self.platform = platform
        self.rank = rank
        self.year = year
        self.genre = genre
        self.publisher = publisher
        self.global_sales = global_sales

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return GameSales.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def custom_guery(self, query):
        return self.query()

    def get_dict_repr(self):
        return {
            'rank': self.rank,
            'name': self.name,
            'platform': self.platform,
            'year': self.year,
            'publisher': self.publisher,
            'genre': self.genre,
            'global_sales': self.global_sales,
            'date_created': self.date_created,
            'date_modified': self.date_modified}