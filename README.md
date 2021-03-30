# Marxist Tweet Generator

Live Link: [Marxist Tweets](http://markov.marx.mtifak.io/)

A tweet generator that uses markov chains to generate renadom sentences based off the corpus fed.

### Tools Used
- __Frontend__ - [JavaScript](https://www.w3schools.com/js/)
- __Backend__ - [Python](https://www.python.org/doc/)

## Build
`docker build -t tweetgen_docker .`

## Run
`docker run -p 5000:5000 --rm --name tweetgen_docker tweetgen_docker`

