# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from core.environment import ENV
from core.core_conf import CoreConf
from api.app import init_app
import api.endpoints.v1

env = ENV()
core_conf = CoreConf()

SQLALCHEMY_DATABASE_URI = env.get_db_uri()

app = init_app({
    "SQLALCHEMY_DATABASE_URI": SQLALCHEMY_DATABASE_URI,
    "CORE_CONF": core_conf
})

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
