fetch('/api/docs')
  .then(response => response.json())
  .then(projects => {
    const container = document.getElementById('projects-container');
    projects.forEach(projet => {
      // créer un élément HTML pour le projet
      const card = document.createElement('div');
      card.classList.add('project-card');
      card.innerHTML = `
        <h3>${projet.titre}</h3>
        <p>${projet.description}</p>
      `;
      container.appendChild(card);
    });
  });
  