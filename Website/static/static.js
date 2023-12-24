const workouts = [
    {
      name: 'Bench Press',
      muscle: 'chest',
      equipment: 'barbells',
      description: 'Lie on a bench and push the barbell away from your chest.'
    },
    {
      name: 'Pull-Ups',
      muscle: 'back',
      equipment: 'bodyweight',
      description: 'Hang from a bar and pull your body up to the bar.'
    },
    // Add more workout data here
  ];

  // Function to filter and display workouts based on selected filters
  function displayWorkouts() {
    const muscleFilter = document.getElementById('muscleFilter').value;
    const equipmentFilter = document.getElementById('equipmentFilter').value;
    const workoutsContainer = document.getElementById('workouts');

    // Clear previous workouts
    workoutsContainer.innerHTML = '';

    workouts.forEach(workout => {
      if ((muscleFilter === 'all' || workout.muscle === muscleFilter) &&
          (equipmentFilter === 'all' || workout.equipment === equipmentFilter)) {
        const workoutElement = document.createElement('div');
        workoutElement.innerHTML = `
          <h2>${workout.name}</h2>
          <p><strong>Muscle Group:</strong> ${workout.muscle}</p>
          <p><strong>Equipment:</strong> ${workout.equipment}</p>
          <p>${workout.description}</p>
        `;
        workoutsContainer.appendChild(workoutElement);
      }
    });
  }

  // Attach event listeners to filters to update workouts on change
  document.getElementById('muscleFilter').addEventListener('change', displayWorkouts);
  document.getElementById('equipmentFilter').addEventListener('change', displayWorkouts);

  // Display initial workouts on page load
  displayWorkouts();