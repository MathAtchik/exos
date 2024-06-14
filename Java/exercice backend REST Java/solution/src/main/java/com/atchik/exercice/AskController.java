package com.atchik.exercice;

import org.springframework.web.bind.annotation.*;

@RestController
public class AskController {

    @PostMapping("/ask")
    public Response ask(@RequestBody Question question) {
        // Simuler une réponse
        String simulatedAnswer = "This is a simulated response to: " + question.getQuery();
        return new Response(simulatedAnswer);
    }

    // Classe interne pour Question
    public static class Question {
        private String query;

        // Getters et Setters
        public String getQuery() {
            return query;
        }

        public void setQuery(String query) {
            this.query = query;
        }
    }

    // Classe interne pour Response
    public static class Response {
        private String answer;

        public Response(String answer) {
            this.answer = answer;
        }

        // Getters et Setters
        public String getAnswer() {
            return answer;
        }

        public void setAnswer(String answer) {
            this.answer = answer;
        }
    }
}