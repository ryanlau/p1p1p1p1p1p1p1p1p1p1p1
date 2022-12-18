shave(".news-title", 24)
shave(".news-summary", 72)

addEventListener("resize", () => {
    shave(".news-title", 24)
    shave(".news-summary", 72)
});
