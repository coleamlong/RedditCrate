import React, { useState } from 'react'

import Container from 'react-bootstrap/Container'
import Modal from 'react-bootstrap/Modal'
import Button from 'react-bootstrap/Button'
import Image from 'react-bootstrap/Image'
import Spinner from 'react-bootstrap/Spinner'

import Logos from '../assets/Logos.png'

const RedditCrate = () => {
    const UserStatus = {
        DEFAULT: 0,
        LOADING: 1,
        SPOTIFY_CONNECTED: 2,
        REDDIT_COMPLETE: 3,
        SPOTIFY_COMPLETE: 4,
        SPOTIFY_CONNECT_ERROR: 5,
        REDDIT_ERROR: 6,

    }

    const [userStatus, setUserStatus] = useState(0)

    const handleClick = () => {
        setUserStatus(UserStatus.SPOTIFY_CONNECTED)
    }

    return (
        <Container className='col-md-3 justify-content-md-center'>
            <Modal.Dialog>
                <Image fluid src={Logos} />
                <br/>
                
                <Modal.Header>
                    <h1>RedditCrate</h1>
                </Modal.Header>

                <Modal.Body>
                    <p>
                        Welcome to RedditCrate! With this tool, you can generate a personal Spotify playlist filled
                        with new and unqiue music pulled from the popular subreddit r/ListenToThis!
                    </p>

                    <p>
                        Listened to all of the songs on your playlist? Complete the steps again to refill the playlist 
                        with more songs!
                    </p>
                    <div className='text-center'>
                        {userStatus === UserStatus.DEFAULT && <p>Connect your Spotify to start!</p>}
                        {userStatus === UserStatus.SPOTIFY_CONNECTED && <p>Spotify is connected! Click to make your playlist.</p>}
                        {userStatus === UserStatus.REDDIT_COMPLETE && <p>Spotify is connected! Creating playlist...</p>}
                        {userStatus === UserStatus.SPOTIFY_COMPLETE && <p>Playlist filled. Check your Spotify!</p>}
                    </div>
                    
                </Modal.Body>

                <Modal.Footer className='justify-content-md-center'>
                    <Button onClick={() => {
                        handleClick()
                        if (userStatus === UserStatus.DEFAULT) {
                            // set button style to loading
                            // call spotify auth code
                            // on success, set status to SPOTIFY_CONNECTED
                            // on fail, set status to SPOTIFY_CONNECT_ERROR
                        } else if (userStatus === UserStatus.SPOTIFY_CONNECTED) {
                            // set button style to loading
                            // call reddit scrape code
                            // on success, set status to REDDIT_COMPLETED
                            // on fail, set status to REDDIT_ERROR
                        }
                    }} variant='primary'>{
                        userStatus === UserStatus.DEFAULT ? 'Connect to Spotify' : 
                        userStatus === UserStatus.LOADING ? (<Spinner animation="border" />) :
                        userStatus === UserStatus.SPOTIFY_CONNECTED ? 'Generate Playlist' : 
                        userStatus === UserStatus.REDDIT_COMPLETE ? (<Spinner animation="border" />) : 
                        userStatus === UserStatus.SPOTIFY_COMPLETE ? 'Done!' : 
                        userStatus === UserStatus.SPOTIFY_CONNECT_ERROR ? 'Error' : 
                        userStatus === UserStatus.REDDIT_ERROR ? 'Error' : 'ERR'
                    }</Button>
                </Modal.Footer>
            </Modal.Dialog>
        </Container>
    )
}

export default RedditCrate