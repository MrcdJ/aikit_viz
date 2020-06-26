from flask import Flask
from flask_restplus import Api, Resource
from aikit.ml_machine import AutoMlResultReader, FolderDataPersister, read_results, read_results_and_errors


app = Flask(__name__)
api = Api(
    app, version='1.0', title='Aikit API',
    description='A first version of aikit API',
)

ns = api.namespace('aikit_api', description='Aikit API operations')


@ns.route('/')
class Home(Resource):
    """ Home for aikit framework """
    @ns.doc('home')
    def get(self):
        """ displays existing aikit results in json format.
            We guess we already have the directory 'titanic', where results files of automl run command are stored.
        """
        result_reader = AutoMlResultReader(FolderDataPersister(base_folder="./titanic/"))
        data_frame = read_results(result_reader)
        return data_frame.to_json()


@ns.route('/errors/')
class Home(Resource):
    """ If we want errors of aikit automl launcher """
    @ns.doc('errors')
    def get(self):
        """ displays existing aikit results and errors in json format.
            We guess we already have the directory 'titanic', where results files are stored.
        """
        result_reader = AutoMlResultReader(FolderDataPersister(base_folder="./titanic/"))
        data_frame_results, data_frame_errors = read_results_and_errors(result_reader)
        return {
            'results': data_frame_results.to_json(),
            'errors': data_frame_errors.to_json()
        }


if __name__ == '__main__':
    app.run(debug=True)

