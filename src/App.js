import logo from './logo.svg';
import './App.css';
import { Authenticator, useAuthenticator } from '@aws-amplify/ui-react';
import '@aws-amplify/ui-react/styles.css';

const Home = () => {
  const { user, signOut } = useAuthenticator((context) => [context.user]);

  return (
    <>
      <h2>Welcome, {user.username}!</h2>
      <button onClick={signOut}>Sign Out</button>
    </>
  );
};

function App() {
  const { authStatus } = useAuthenticator(context => [context.authStatus]);
  return (
    <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          {authStatus === 'configuring' && 'Loading...'}
          {authStatus !== 'authenticated' ? <Authenticator /> : <Home />}
        </header>
    </div> 

    
  );
}

export default App;
