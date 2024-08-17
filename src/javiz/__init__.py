try:
    from dotenv import load_dotenv

    load_dotenv()

except Exception:
    pass

from mangum import Mangum
from javiz.main import app

handler = Mangum(app)
