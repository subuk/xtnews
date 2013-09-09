
from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from models import DBSession, Base

def main(global_config, **settings):
    config = Configurator(settings=settings)

    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)

    config.include('pyramid_jinja2')

    config.add_route('item', '/{id}')
    config.add_route('list', '/')

    config.scan('xtnews.views')
    return config.make_wsgi_app()

