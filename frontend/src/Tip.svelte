<script>
  import { fade, fly } from "svelte/transition";
  import CopyToClipboard from "svelte-copy-to-clipboard";

  export let tip;
  export let show_all;
  export let setMedia;
  export let markRead;

  let copyText = "Copy URL";

  const CATEGORYS = {
    0: "web",
  };
</script>

{#if show_all || !tip.read}
  <div class="p-2 -m-1 group" out:fade>
    <div class="overflow-auto bg-white border-2 border-gray-300 rounded-lg">
      <div class="relative p-2">
        {#if tip.media}
          <img
            class="object-cover object-center w-full rounded-lg lg:h-48 md:h-36"
            src={tip.media}
            on:click={(e) => setMedia(tip.media)}
            alt={tip.title} />
        {/if}
        {#if !tip.read}
          <div
            class="absolute top-0 right-0 flex items-center justify-center h-10 m-2">
            <button
              on:click={(e) => markRead(tip)}
              class="flex items-center justify-center invisible w-10 h-10 p-0 border-0 rounded-full group-hover:visible group-hover:inline-flex group-hover:text-white group-hover:bg-green-400">
              <svg
                class="w-6 h-6"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg">
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M5 13l4 4L19 7" />
              </svg>
            </button>
          </div>
        {/if}
      </div>
      <div class="p-6">
        <h1 class="mb-3 text-lg font-medium text-gray-900 title-font">
          <a href={tip.url} target="_blank" class="flex flex-col text-gray-900">
            <span class="font-semibold ">{tip.title}</span>
            <div class="flex items-center">
              <svg
                class="w-3 h-3 mr-1"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg">
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656
                  5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0
                  00-5.656-5.656l-1.1 1.1" />
              </svg>
              <span class="text-sm text-indigo-600 underline">{tip.url}</span>
            </div>
          </a>
        </h1>
        <h2
          class="mb-4 -mt-1 text-xs font-medium tracking-widest text-gray-500 title-font">
          {tip.created_at}
        </h2>
        <p class="mb-3 leading-relaxed whitespace-pre-wrap">
          {@html tip.content}
        </p>
        <div class="flex flex-wrap items-center justify-between">
          <span class="px-1 text-white bg-indigo-500 rounded-lg">
            {CATEGORYS[tip.category]}
          </span>
          <div>
            <span
              class="py-1 pr-3 mr-3 text-sm leading-none text-gray-600 border-r-2 border-gray-300 lg:ml-auto md:ml-0">
              <CopyToClipboard
                text={tip.url}
                on:copy={() => (copyText = 'Copied!')}
                let:copy>
                <button on:click={copy} class="inline-flex items-center">
                  <svg
                    class="w-4 h-4 mr-1"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                    xmlns="http://www.w3.org/2000/svg"><path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" /></svg>
                  {copyText}
                </button>
              </CopyToClipboard>
            </span>
            {#if !tip.read}
              <span
                class="inline-flex items-center py-1 pr-3 ml-auto mr-3 text-sm leading-none text-red-600 border-r-2 border-gray-300 lg:ml-auto md:ml-0">
                <svg
                  class="w-4 h-4 mr-1"
                  stroke="currentColor"
                  stroke-width="2"
                  fill="none"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  viewBox="0 0 24 24">
                  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z" />
                  <circle cx="12" cy="12" r="3" />
                </svg>
                Unread
              </span>
            {:else}
              <span
                class="inline-flex items-center py-1 pr-3 ml-auto mr-3 text-sm leading-none text-green-500 border-r-2 border-gray-300 lg:ml-auto md:ml-0">
                <svg
                  class="w-4 h-4 mr-1"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                  xmlns="http://www.w3.org/2000/svg">
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                Read
              </span>
            {/if}
            <span
              class="inline-flex items-center text-sm leading-none text-gray-600">
              <a href={tip.origin} target="_blank" class="flex items-center">
                <svg
                  class="w-4 h-4 mr-1"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  stroke-width="2"
                  fill="none"
                  stroke-linecap="round"
                  stroke-linejoin="round">
                  <path d="M5 12h14" />
                  <path d="M12 5l7 7-7 7" />
                </svg>
                Source
              </a>
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
{/if}
