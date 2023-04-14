"""test reource
"""

from flask_restful import Resource

class Test(Resource):
    """Test resource class
    """
    def get(self):
        """Test resource

        Returns:
            dict: sample message
        """
        return {"message": "API is running!"}
