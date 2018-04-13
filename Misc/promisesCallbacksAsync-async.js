const fetch = require("/Users/jmartin/.nvm/versions/node/v8.9.3/lib/node_modules/node-fetch");

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

async function getTwoRandomGithubUsers() {
  try {
    // Pick a random user
    const response = await fetch(`${GITHUB_ENDPOINT}/users`);
    const users = await response.json();
    if (response.status !== 200) throw new Error(users.message);

    // Get total list of first user's repos
    const user1 = users[getRandomInt(users.length)];
    const user1Repos = await (await fetch(user1.repos_url)).json();

    // Pick a random repo
    const randomRepo = user1Repos[getRandomInt(user1Repos.length)];
    if (!randomRepo || !randomRepo.watchers) throw new Error(randomRepo ? `${randomRepo.full_name} has no watchers=(` : `No valid repos`);

    // Pick a random second user from the list of subscribers
    const randomRepoSubscribers = await (await fetch(randomRepo.subscribers_url)).json();
    const user2 = randomRepoSubscribers[getRandomInt(randomRepoSubscribers.length)];

    // Get total list of second user's repos
    const user2Repos = await (await fetch(user2.repos_url)).json();

    printResults(
      Object.assign({}, user1, { repo_count: user1Repos.length }),
      Object.assign({}, user2, { repo_count: user2Repos.length }),
      randomRepo
    );
  } catch (error) {
    console.error(error);
  }
}

getTwoRandomGithubUsers();