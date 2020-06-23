from flask import Flask
from flask_restplus import Api, Resource
from utils import utils


app = Flask(__name__)
api = Api(
    app, version='1.0', title='Aikit API',
    description='A first version of aikit API',
)

ns = api.namespace('aikit_api', description='Aikit API operations')


response = api.model('response', utils.swagger_Result())

# todo: swagger
#  config = api.model('Config', FactoryDAO().swagger_ConfigDAO())


@ns.route('/')
class Home(Resource):
    """ Home for aikit framework"""
    @ns.doc('home')
    @api.marshal_with(response)
    def get(self):
        """ List all aikit options """  # todo: for now, just display existing aikit result in json format
        file = "./result.xlsx"
        return {'result': utils.xl_to_Result(file)}

#     @ns.doc('aikit config and run')
#     #@ns.expect(config)
#     #@ns.marshal_with(config, code=201)
#     def post(self):
#         """Define parameters for aikit configuration and launch the research"""
#         # todo: working on it
#         # return Client_Session.to_json()
#
#
# # TODO: give id to client and save aikit run in id path
# @ns.route('/<int:id>')
# @ns.response(404, 'Id not found')
# @ns.param('id', 'The client path identifier')
# class Result(Resource):
#     """Shows a list of client own aikit results"""
#     @ns.doc('list_results')
#     @ns.marshal_list_with(result)
#     def get(self):
#         """List all results"""
#         # todo: get what is done is route('/')


if __name__ == '__main__':
    app.run(debug=True)

