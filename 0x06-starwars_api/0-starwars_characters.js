#!/usr/bin/node

const request = require('request');

/**
 * Makes a request to a given URL and prints the character's name.
 * @param {string[]} urls - The list of character URLs.
 * @param {number} index - The current index in the list of URLs.
 */
const fetchCharacter = (urls, index) => {
  if (index === urls.length) return;

  request(urls[index], (error, response, body) => {
    if (error) {
      console.error(`Error fetching character: ${error.message}`);
      return;
    }

    try {
      const character = JSON.parse(body);
      console.log(character.name);
    } catch (parseError) {
      console.error(`Error parsing response: ${parseError.message}`);
    }

    fetchCharacter(urls, index + 1);
  });
};

/**
 * Fetches and prints all characters of a Star Wars movie by its ID.
 */
const fetchMovieCharacters = () => {
  const movieId = process.argv[2];

  if (!movieId) {
    console.error('Please provide a Movie ID');
    return;
  }

  const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

  request(url, (error, response, body) => {
    if (error) {
      console.error(`Error fetching movie: ${error.message}`);
      return;
    }

    try {
      const movie = JSON.parse(body);
      const characters = movie.characters;
      fetchCharacter(characters, 0);
    } catch (parseError) {
      console.error(`Error parsing response: ${parseError.message}`);
    }
  });
};

fetchMovieCharacters();
