<template>
  <div class="min-h-screen bg-[#faf7f2] text-[#5C3B28]">
    <header class="border-b border-[#d7c2b0] p-6">
      <div class="flex items-center justify-between">
        <div>
          <h1 class="text-3xl font-bold">SyncForge</h1>
          <p class="text-sm">AI Workplace Intelligence</p>
        </div>

        <button class="bg-[#5C3B28] text-white px-5 py-2 rounded-xl">
          Get Started
        </button>
      </div>
    </header>

    <main class="p-10">
      <h2 class="text-5xl font-black leading-tight">
        Smarter Engineering Teams
      </h2>

      <p class="mt-6 text-lg max-w-2xl">
        Productivity analytics, burnout detection, contribution scoring,
        proof-of-work reports, and AI-powered workplace intelligence.
      </p>

      <div class="grid grid-cols-2 gap-6 mt-10">
        <div
          v-for="metric in metrics"
          :key="metric.title"
          class="bg-white p-6 rounded-3xl shadow"
        >
          <p class="text-sm opacity-70">
            {{ metric.title }}
          </p>

          <h3 class="text-3xl font-bold mt-2">
            {{ metric.value }}
          </h3>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: "App",

  data() {
    return {
      metrics: [
        {
          title: "Contribution Score",
          value: "92%",
        },
        {
          title: "Collaboration Index",
          value: "88%",
        },
        {
          title: "Focus Score",
          value: "81%",
        },
        {
          title: "Burnout Risk",
          value: "Low",
        },
      ],
    };
  },
};
</script>

<style>
body {
  margin: 0;
  font-family: Arial, sans-serif;
}
</style>