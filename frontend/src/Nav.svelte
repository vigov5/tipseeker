<script>
  export let show_all;
  export let unread_count;

  $: button_text = show_all ? "Hide Read" : "Show All";
</script>

<header
  class="fixed top-0 left-0 z-50 w-full text-gray-700 bg-white border-b-2 border-blue-500 body-font">
  <div
    class="container flex flex-col flex-wrap items-center p-2 mx-auto md:flex-row">
    <a
      href="/"
      class="flex items-center mb-4 font-medium text-gray-900 title-font md:mb-0">
      <svg
        class="w-10 h-10 p-2 text-white bg-indigo-500 rounded-full"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
        xmlns="http://www.w3.org/2000/svg">
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4
          12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374
          3.374 0 0014 18.469V19a2 2 0 11-4
          0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
      </svg>
      <span class="ml-3 text-xl">Tipseeker</span>
    </a>
    <nav
      class="flex flex-wrap items-center justify-center text-base md:mr-auto md:ml-4 md:py-1 md:pl-4 md:border-l md:border-gray-400">
      <strong>{unread_count}</strong>
      &nbsp;unread tips remaining
    </nav>
    <button
      class="inline-flex items-center px-3 py-1 mt-4 text-base bg-gray-200 border-0 rounded focus:outline-none hover:bg-gray-300 md:mt-0"
      on:click={e => (show_all = !show_all)}>
      {button_text}
    </button>
  </div>
</header>
