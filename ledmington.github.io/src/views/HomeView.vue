<script setup>
import CardGrid from "../components/CardGrid.vue";
import MainCard from "../components/MainCard.vue";
import PhotoCard from "../components/PhotoCard.vue";
</script>

<template>
  <main>
    <CardGrid>
      <MainCard>
        <template #title>Skills</template>
        <template #content>C, Java, Python<br />CUDA, OpenMP, MPI</template>
      </MainCard>

      <PhotoCard>
        <template #photo
          ><img
            alt="Profile photo"
            class="logo"
            src="@/assets/img/profile.jpeg"
        /></template>
        <template #location>Riccione, Italy</template>
        <template #email>filippo.barbari@gmail.com</template>
        <template #url>https://ledmington.github.io</template>
      </PhotoCard>

      <MainCard>
        <template #title>Mottos</template>
        <template #content>
          <p>
            <i>If a computer can do it, a computer should do it.</i><br />&mdash;
            Robert C. Martin AKA Uncle Bob
          </p><br />
          <p>
            <i>The only way to go fast is to go well.</i><br />&mdash; Robert C.
            Martin AKA Uncle Bob
          </p><br />
          <p>
            <i>Your first 10,000 photographs are your worst.</i><br />&mdash;
            Henri Cartier-Bresson
          </p>
        </template>
      </MainCard>

      <MainCard>
        <template #title>About</template>
        <template #content
          >Developer and master student at University of Bologna. Algorithms and
          Data Structures enthusiast. I love esoteric languages, board games and
          parallel simulations.</template
        >
      </MainCard>

      <MainCard>
        <template #title>Projects</template>
        <template #content
          >Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime
          mollitia, molestiae quas vel sint commodi repudiandae consequuntur
          voluptatum laborum numquam blanditiis harum quisquam eius sed odit
          fugiat iusto fuga praesentium optio, eaque rerum!</template
        >
      </MainCard>

      <MainCard>
        <template #title>Work Experience</template>
        <template #content
          >Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime
          mollitia, molestiae quas vel sint commodi repudiandae consequuntur
          voluptatum laborum numquam blanditiis harum quisquam eius sed odit
          fugiat iusto fuga praesentium optio, eaque rerum!</template
        >
      </MainCard>

      <MainCard>
        <template #title>Education</template>
        <template #content
          >Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime
          mollitia, molestiae quas vel sint commodi repudiandae consequuntur
          voluptatum laborum numquam blanditiis harum quisquam eius sed odit
          fugiat iusto fuga praesentium optio, eaque rerum!</template
        >
      </MainCard>
    </CardGrid>
  </main>
</template>
