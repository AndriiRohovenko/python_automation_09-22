from pony.orm import Database


base = Database()

base.bind(provider='postgres', user='postgres', password='postgres', host='localhost', database='test')
