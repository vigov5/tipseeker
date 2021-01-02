<script>
  import InfiniteScroll from "svelte-infinite-scroll";
  import Nav from "./Nav.svelte";
  import Tip from "./Tip.svelte";
  import { onMount } from "svelte";
  import { BASE_URL } from "./config";

  let tips = [];
  let page = 1;
  let newBatch = [];
  let show_all = false;
  let viewing_media = "";
  let unread_count = 0;

  const fetchData = async () => {
    const res = await fetch(`${BASE_URL}/link/?page=${page}`);
    let resp = await res.json();
    newBatch = resp.links;
    unread_count = resp.unread_count;
  };

  onMount(() => {
    fetchData();
  });

  const setMedia = (media) => {
    console.log(media);
    viewing_media = media;
  };

  const markRead = async (tip, rating) => {
    let ret = await (
      await fetch(`${BASE_URL}/link/mark_read`, {
        method: "POST",
        body: JSON.stringify({
          id: tip.id,
          rating: rating,
        }),
      })
    ).json();

    if (ret["status"] == "OK") {
      unread_count = ret["unread_count"];
      tips.map((t) => {
        if (t.id == tip.id) (t.read = 1), (tip.rating = rating ? 1 : 2);
      });
      tips = tips;
    }
  };

  $: tips = [...new Set([...tips, ...newBatch])];
</script>

<style>
</style>

<svelte:head>
  <title>Tipseeker</title>
</svelte:head>

<main class="min-h-screen -m-2 bg-gray-200">
  <Nav bind:show_all {unread_count} />
  {#if viewing_media}
    <div
      class="fixed z-50 max-h-screen origin-center transform -translate-x-1/2 -translate-y-1/2"
      style="left: 50%; top: 50%;">
      <img class="border border-gray-500" src={viewing_media} alt="" />
      <div
        class="absolute top-0 right-0 m-2 bg-white rounded-full"
        on:click={(e) => (viewing_media = '')}>
        <svg viewBox="0 0 20 20" fill="currentColor" class="w-6 h-6">
          <path
            fill-rule="evenodd"
            d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414
            1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293
            4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
            clip-rule="evenodd" />
        </svg>
      </div>
    </div>
  {/if}
  <section class="container max-w-4xl mx-auto mt-4 text-gray-700 body-font">
    <div class="px-5 py-10 mx-auto">
      <div class="mt-4">
        {#if !tips}
          No content
        {:else}
          {#each tips as tip}
            <Tip {tip} {show_all} {setMedia} {markRead} />
          {/each}
          <InfiniteScroll
            window={true}
            threshold={100}
            on:loadMore={() => {
              page++;
              fetchData();
            }} />
        {/if}
      </div>
    </div>
  </section>
</main>
