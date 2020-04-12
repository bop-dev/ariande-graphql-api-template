from ariadne import load_schema_from_path, ObjectType, QueryType, MutationType
from features.Hangs.hang import resolve_hang, create_hang, update_hang


hangQueries = QueryType()
hangMutations = MutationType()

hangTypes = load_schema_from_path("./features/Hangs/hang.gql")
hangObjectType = ObjectType('HTHang')
hangQueries.set_field('getHang', resolve_hang)
hangMutations.set_field('createHang', create_hang)
hangMutations.set_field('updateHang', update_hang)
