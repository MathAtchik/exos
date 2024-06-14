package com.atchik.exercice;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class CorsConfig {

    /*
    Ce fichier sert à configurer l'application pour accepter les appels de n'importe quelle origine
    Sans ce fichier, l'application refuse les appels depuis un navigateur extérieur pour des questions de sécurité
    Lire la documentation sur les en-tête CORS : https://developer.mozilla.org/fr/docs/Web/HTTP/CORS/Errors/CORSMissingAllowOrigin
     */

    @Bean
    public WebMvcConfigurer corsConfigurer() {
        return new WebMvcConfigurer() {
            @Override
            public void addCorsMappings(CorsRegistry registry) {
                registry.addMapping("/ask")
                        .allowedOrigins("*") // Remplacez l'URL par celle de votre frontend
                        .allowedMethods("GET", "POST", "PUT", "DELETE", "OPTIONS")
                        .allowedHeaders("*")
                        .allowCredentials(false);
            }
        };
    }
}