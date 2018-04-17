// const json = require('./test.json');

// console.log(json);

const json = {
    "name": "WorkoutType",
    "value": "abs",
    "resolutions": {
        "resolutionsPerAuthority": [
            {
                "authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.2666df7d-e3b4-4f20-89c7-ac3ad1ea8cf3.workout_type",
                "status": {
                    "code": "ER_SUCCESS_MATCH"
                },
                "values": [
                    {
                        "value": {
                            "name": "core",
                            "id": "core"
                        }
                    }
                ]
            }
        ]
    },
    "confirmationStatus": "NONE"
};

try {
    const {resolutions: { resolutionsPerAuthority: [{status: { code }}] } } = json;
    console.log(code);
    if (code !== "ER_SUCCESS_MATCH") throw new Error("Not a match");

    const {resolutions: { resolutionsPerAuthority: [{values: [ { value: { id } }]}] } } = json;
    console.log(`Status Code: ${code} | ID: ${id}`);
} catch(e) {
    console.warn("Error accessing ID", e)
}