/**
 * @jest-environment jsdom
 */

const findPercentageForAffix = require("../script");

// rest of your code



const fs = require('fs');
const { async } = require('rsvp');
let affixPerc;

beforeEach(async () => {
    const rawdata = await fs.readFileSync('./static/json/affix.json');
    affixPerc = await JSON.parse(rawdata);
});


describe("findPercentageForAffix", () => {

    it("should return true for an affix with percentage 'true'", async () => {
        console.log(affixPerc);
        expect(findPercentageForAffix("barrier generation")).toBe(true);
    }
    );
});