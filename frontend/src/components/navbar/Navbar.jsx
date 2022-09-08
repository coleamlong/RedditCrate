import React from 'react'
import Container from 'react-bootstrap/Container'
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar'

const TopNavbar = () => {
  return (
    <>
        <Navbar variant="light">
            <Container>
                <Nav className="col justify-content-center">
                    <Nav.Link href="#home">Home</Nav.Link>
                    <Nav.Link href="#about">About</Nav.Link>
                    <Nav.Link href="#projects">Projects</Nav.Link>
                    <Nav.Link href="#skills">Skills</Nav.Link>
                    <Nav.Link href="#contact">Contact</Nav.Link>
    
                </Nav>
            </Container>
        </Navbar>
    </>
  )
}

export default TopNavbar