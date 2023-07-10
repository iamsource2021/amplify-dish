import logo from './logo.svg';
import './App.css';
import { Authenticator, useAuthenticator, Flex, View } from '@aws-amplify/ui-react';
import '@aws-amplify/ui-react/styles.css';
import {
  Features2x2
} from './ui-components';



function Home() {
  const { user, signOut } = useAuthenticator((context) => [context.user]);

  return (
    <>
      <View
        id="servicios"
        height="auto"
        width="100%"
      >

        <h2>Welcome, {user.attributes.email}!</h2>
        <button onClick={signOut}>Sign Out</button>
      </View>
      <View
        height="auto"
        width="100%"
        id="recursos"
      >
        <Features2x2 overrides={
          {
            Features2x2: {
              width: "100%",
            }
          }
        } />
      </View>
    </>

  );
}

function App() {
  const { authStatus } = useAuthenticator(context => [context.authStatus]);
  return (
    <Flex
      direction="column"
      justifyContent="flex-start"
      alignItems="stretch"
      alignContent="flex-start"
      wrap="nowrap"
      gap="0"
    >
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          {authStatus === 'configuring' && 'Loading...'}
          {authStatus !== 'authenticated' ? <Authenticator /> : <Home />}
        </header>
      </div>
    </Flex>



  );
}

export default App;
