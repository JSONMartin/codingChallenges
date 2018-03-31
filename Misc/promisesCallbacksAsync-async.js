const fetch = require("/Users/jmartin/.nvm/versions/node/v8.9.3/lib/node_modules/node-fetch");

const GITHUB_ENDPOINT = "https://api.github.com";
const getRandomInt = max => Math.floor(Math.random() * Math.floor(max));

function printResults(user1, user2, randomRepo) {
  console.log(`Picked first random Github user: ${user1.login} | Repo Count: ${user1.repo_count}`);
  console.log(`Picked random repo: ${randomRepo.full_name}, which has ${randomRepo.watchers} watchers`);
  console.log(`Picked second random person watching this repo: ${user2.login} | Repo Count:${user2.repo_count}`);
}

async function getTwoRandomGithubUsers() {
  try {
    // Pick a random user
    const users = await (await fetch(`${GITHUB_ENDPOINT}/users`)).json();
    const user1 = users[getRandomInt(users.length)]

    // Get total list of first user's repos
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
    console.log(error);
  }
}

getTwoRandomGithubUsers();