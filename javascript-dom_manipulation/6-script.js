fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => {
    if (!response.ok) {
      throw new Error(`Erreur HTTP: ${response.status}`);
    }
    return response.json()
  })
  .then(data => {
    document.getElementById('character').textContent = data.name;
  })
  .catch(error => {
    console.error(`Error: ${error}`);
  });
