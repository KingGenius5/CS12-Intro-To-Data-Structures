# Marxist Tweet Generator

Live Link: [Marxist Tweets](http://markov.marx.mtifak.io/)

A tweet generator that uses markov chains to generate renadom sentences based off the corpus fed.

## Build
`docker build -t tweetgen_docker .`

## Run
`docker run -p 5000:5000 --rm --name tweetgen_docker tweetgen_docker`

## Health Check
 Sending `GET` request to `/health` should return `{ "Status" : "200 OK" }`

