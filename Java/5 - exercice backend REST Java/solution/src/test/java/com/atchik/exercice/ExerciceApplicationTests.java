package com.atchik.exercice;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;

import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@SpringBootTest
@AutoConfigureMockMvc
class ExerciceApplicationTests {

	@Autowired
	private MockMvc mockMvc;

	@Test
	void contextLoads() {
	}

	@Test
	void testAskControllerEndpoint() throws Exception {
		// Préparer la requête JSON
		String questionJson = "{\"query\": \"What is the capital of France?\"}";

		// Effectuer une requête POST vers /ask et vérifier la réponse
		mockMvc.perform(MockMvcRequestBuilders.post("/ask")
						.contentType(MediaType.APPLICATION_JSON)
						.content(questionJson))
				.andExpect(status().isOk())
				.andExpect(content().contentType(MediaType.APPLICATION_JSON))
				.andExpect(content().json("{\"answer\": \"This is a simulated response to: What is the capital of France?\"}"));
	}
}
