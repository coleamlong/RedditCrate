import TopNavbar from './components/navbar/Navbar'
import Header from './layouts/header/Header'
import Stack from 'react-bootstrap/Stack'

import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <>
      <TopNavbar />
      <Stack gap={0}>
        <Header />
      </Stack>
    </>
  )
}

export default App;
