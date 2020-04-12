from ariadne import QueryType, make_executable_schema, graphql_sync, MutationType
from ariadne import load_schema_from_path
from features.Hangs.hangTypes import hangTypes, hangObjectType, hangQueries, hangMutations
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify
from features.Hangs.hang import create_hang, resolve_hang, update_hang
queryTypes = load_schema_from_path("./root_types/queries.gql")
mutationTypes = load_schema_from_path("./root_types/mutations.gql")

schema = make_executable_schema(
    [mutationTypes, queryTypes, hangTypes],
    [hangObjectType, hangQueries, hangMutations]
)

app = Flask(__name__)

@app.route("/graphql", methods=["GET"])
def graphql_playgroud():
    return PLAYGROUND_HTML


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    return jsonify(result)