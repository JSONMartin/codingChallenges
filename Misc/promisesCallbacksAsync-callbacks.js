// Pick a random user from the list of all users on Github
// Then pick a random repo for the user
// If the random repo has watchers, grab a list of the watchers (otherwise stop here)
// Pick a random user who is watching the selected repo
// Once we have all of the data, print out the first user's info, their randomly selected repo, and the second user's info.
const $ = require("jquery");

const GITHUB_ENDPOINT = "https://api.github.com";
const getRandomInt = max => Math.floor(Math.random() * Math.floor(max));

function printResults(user1, user2, randomRepo) {
  const results = `Picked first random Github user: ${user1.login} | Repo Count: ${user1.repo_count}

    Picked random repo: ${randomRepo.full_name}, which has ${randomRepo.watchers} watchers

    Picked second random person watching this repo: ${user2.login} | Repo Count:${user2.repo_count}
`;

  $(`<hr>${results.replace(/\r|\n/g, '<br />')}</hr>`).appendTo("#results");
  console.log(results);
}

function getTwoRandomGithubUsers() {
  // Pick a random user
  $.ajax({
    url: `${GITHUB_ENDPOINT}/users`,
    success: function(users) {
      const user1 = users[getRandomInt(users.length)];

      // Get total list of user1's repos
      $.ajax({
        url: user1.repos_url,
        success: function(user1Repos) {
          const randomRepo = user1Repos[getRandomInt(user1Repos.length)];

          if (randomRepo.watchers > 0) {
            // Pick a random subscriber
            $.ajax({
              url: randomRepo.subscribers_url,
              success: function(randomRepoSubscribers) {
                if (randomRepoSubscribers.length < 1) {
                  console.error( `${randomRepo.full_name} has no subscribers =( Aborting`);
                  return false;
                }
                const user2 = randomRepoSubscribers[getRandomInt(randomRepoSubscribers.length)];

                // Get total list of users2's repos
                $.ajax({
                  url: user2.repos_url,
                  success: function(user2Repos) {
                    // THIS is the final place we want to end up - with both User 1 and User 2's data, so we can print the results.
                    printResults(
                      Object.assign({}, user1, { repo_count: user1Repos.length }),
                      Object.assign({}, user2, { repo_count: user2Repos.length }),
                      randomRepo
                    );
                  },
                  error: function(error) {
                    console.error("Errored:", error);
                  }
                });
              },
              error: function(error) {
                console.error("Errored:", error);
              }
            });
          } else {
            console.error(`${randomRepo.full_name} has no subscribers =(!`);
          }
        },
        error: function(error) {
          console.error("Errored:", error);
        }
      });
    },
    error: function(error) {
      console.error("Errored:", error);
    }
  });
}

getTwoRandomGithubUsers();
