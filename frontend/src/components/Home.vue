<script setup>
import { ref } from 'vue';
import Navbar from './Navbar.vue';

const days = ref([
  { date: '26日', message: '信息一' },
  { date: '27日', message: '嗨，你还可以更努力！' },
  { date: '28日', message: '信息三' },
]);

function goToPreviousDay() {
  console.log('前一天');
}

function goToNextDay() {
  console.log('后一天');
}

function doAction(date) {
  console.log('执行操作', date);
}
</script>

<template>
  <div class="container">
    <Navbar/>
    <div class="card-container">
      <div v-for="day in days" :key="day.date" class="day-card">
        <div class="card-header">
          <button @click="goToPreviousDay">←</button>
          <span>{{ day.date }}</span>
          <button @click="goToNextDay">→</button>
        </div>
        <div class="card-body">
          <h2>{{ day.message }}</h2>
          <button @click="doAction(day.date)">来写吧！</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  width: 100vw;
}

.card-container {
  display: flex;
  overflow-x: auto;
  overflow-y: hidden; /* 禁止垂直滚动 */
  white-space: nowrap;
  width: 100%;
  height: 76%; /* 确保这是足够的高度来包含卡片而不溢出 */
}

.day-card {
  flex: 0 0 auto;
  width: 300px; /* 卡片宽度 */
  margin: 10px 10px;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  height: 90%; /* 确保卡片内部不溢出，可能需要调整padding和font-size */
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.card-body {
  text-align: center;
  height: calc(100% - 30px); /* 从总高度减去头部高度 */
}

button {
  padding: 5px 10px;
  margin: 5px;
  background-color: #f0f0f0;
}

@media (max-width: 600px) {
  .day-card {
    width: 90vw; /* 在移动设备上调整宽度 */
  }
}
</style>