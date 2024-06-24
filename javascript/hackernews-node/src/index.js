const { ApolloServer } = require('apollo-server');

// 1
const typeDefs = `
  type Query {
      users: [User!]!
      user(id: ID!): User
      info: String!
    }
    
    type Mutation {
      createUser(name: String!): User!
    }
    
    type User {
      id: ID!
      name: String!
    }
`

// 2
const resolvers = {
    Query: {
        info: () => null,
    }
}

// 3
const server = new ApolloServer({
    typeDefs,
    resolvers,
})

server
    .listen()
    .then(({ url }) =>
        console.log(`Server is running on ${url}`)
    );
