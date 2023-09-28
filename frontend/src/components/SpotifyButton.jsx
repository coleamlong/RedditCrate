import React, { useEffect } from "react";

import { Button } from "react-bootstrap";

const CLIENT_ID = "91d037f7894441b2aab67c0acec6689d";
const SPOTIFY_AUTHORIZE_ENDPOINT = "https://accounts.spotify.com/authorize";
const REDIRECT_URI_AFTER_LOGIN = "http://localhost:3000/";
const SPACE_DELIM = "%20";
const SCOPES = ["playlist-modify-public", "playlist-read-private"];

const SCOPES_URL_PARAM = SCOPES.join(SPACE_DELIM);

const getReturnedParamsFromSpotifyAuth = (hash) => {
    const stringAfterHashtag = hash.substring(1);
    const paramsInUrl = stringAfterHashtag.split("&");
    const paramsSplitUp = paramsInUrl.reduce((accumulater, currentValue) => {
        console.log(currentValue);
        const [key, value] = currentValue.split("=");
        accumulater[key] = value;
        return accumulater;
    }, {});

    return paramsSplitUp;
};

const SpotifyButton = () => {
    useEffect(() => {
        if (window.location.hash) {
            const { access_token, expires_in, token_type } =
                getReturnedParamsFromSpotifyAuth(window.location.hash);
        }
    });
    const handleLogin = () => {
        window.location = `${SPOTIFY_AUTHORIZE_ENDPOINT}?client_id=${CLIENT_ID}&redirect_uri=${REDIRECT_URI_AFTER_LOGIN}&scope=${SCOPES_URL_PARAM}&response_type=token&show_dialog=true`;
    };
    return (
        <div>
            <Button onClick={handleLogin}>Login to Spotify</Button>
        </div>
    );
};

export default SpotifyButton;
