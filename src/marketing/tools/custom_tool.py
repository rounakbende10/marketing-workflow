from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import json
import os

class LinkedInPostAnalyzerInput(BaseModel):
    post_content: str = Field(..., description="The LinkedIn post content to analyze")
    target_audience: str = Field(..., description="The target audience for the post")

class LinkedInPostAnalyzerOutput(BaseModel):
    engagement_score: int = Field(..., description="Predicted engagement score (1-10)")
    hashtag_suggestions: list = Field(..., description="Suggested hashtags for the post")
    optimization_tips: list = Field(..., description="Tips to improve the post")
    target_audience_match: str = Field(..., description="How well the post matches the target audience")

class LinkedInPostAnalyzer(BaseTool):
    name: str = "LinkedIn Post Analyzer"
    description: str = "Analyzes LinkedIn posts for engagement potential and provides optimization suggestions for AI/ML research scientist roles"
    
    def _run(self, post_content: str, target_audience: str) -> str:
        """
        Analyze a LinkedIn post for engagement potential and provide optimization suggestions for AI/ML research scientist roles.
        """
        # This is a simplified analysis - in a real implementation, you might use
        # LinkedIn's API or machine learning models for more accurate predictions
        
        # Basic engagement scoring based on content characteristics
        score = 5  # Base score
        
        # Check for engagement triggers
        if "?" in post_content:
            score += 1
        if "!" in post_content:
            score += 1
        if len(post_content.split()) > 50:
            score += 1
        if "#" in post_content:
            score += 1
        if "https://" in post_content or "http://" in post_content:
            score += 1
            
        # Suggested hashtags based on content for AI/ML research scientist
        hashtags = []
        content_lower = post_content.lower()
        
        # AI/ML Research Scientist specific hashtags
        if "research" in content_lower or "paper" in content_lower:
            hashtags.extend(["#Research", "#AIResearch", "#MLResearch", "#AcademicResearch"])
        if "llm" in content_lower or "large language model" in content_lower:
            hashtags.extend(["#LLM", "#LargeLanguageModels", "#AI", "#MachineLearning"])
        if "rag" in content_lower or "retrieval augmented generation" in content_lower:
            hashtags.extend(["#RAG", "#RetrievalAugmentedGeneration", "#AI", "#NLP"])
        if "innovation" in content_lower or "breakthrough" in content_lower:
            hashtags.extend(["#Innovation", "#AIInnovation", "#ResearchInnovation", "#TechInnovation"])
        if "optimal" in content_lower or "method" in content_lower:
            hashtags.extend(["#OptimalMethods", "#ResearchMethods", "#AI", "#MachineLearning"])
        if "scientist" in content_lower or "research" in content_lower:
            hashtags.extend(["#ResearchScientist", "#AIScientist", "#MLScientist", "#TechResearch"])
        if "pytorch" in content_lower or "tensorflow" in content_lower:
            hashtags.extend(["#PyTorch", "#TensorFlow", "#DeepLearning", "#AI"])
        if "arxiv" in content_lower or "paper" in content_lower:
            hashtags.extend(["#ArXiv", "#ResearchPaper", "#Academic", "#AIResearch"])
        if "healthcare" in content_lower or "clinical" in content_lower:
            hashtags.extend(["#HealthcareAI", "#ClinicalAI", "#HealthTech", "#AI"])
        if "finance" in content_lower or "fintech" in content_lower:
            hashtags.extend(["#FinTech", "#FinanceAI", "#AI", "#MachineLearning"])
            
        # Add general research scientist hashtags
        hashtags.extend(["#LinkedIn", "#AIResearch", "#MachineLearning", "#ResearchScientist", "#TechResearch"])
        
        # Optimization tips for research scientist content
        tips = []
        if score < 7:
            tips.append("Add research depth to demonstrate scientific expertise")
            tips.append("Include relevant research hashtags")
            tips.append("Add a call-to-action for research discussion")
        if len(post_content) < 100:
            tips.append("Expand on research concepts for better engagement")
        if "?" not in post_content:
            tips.append("Ask a research question to encourage comments")
        if "research" not in content_lower and "paper" not in content_lower:
            tips.append("Consider adding research insights")
        if "innovation" not in content_lower and "optimal" not in content_lower:
            tips.append("Include innovation and optimal methods insights")
            
        result = {
            "engagement_score": min(score, 10),
            "hashtag_suggestions": hashtags[:5],
            "optimization_tips": tips,
            "target_audience_match": "Good" if score >= 7 else "Needs improvement"
        }
        
        return json.dumps(result, indent=2)

class AIMLImageGeneratorInput(BaseModel):
    topic: str = Field(..., description="The AI/ML topic or concept to visualize")
    content_type: str = Field(..., description="The type of content (LinkedIn post, research blog)")
    visualization_type: str = Field(..., description="The type of visualization needed (diagram, infographic, flowchart, etc.)")

class AIMLImageGeneratorOutput(BaseModel):
    image_prompts: list = Field(..., description="Optimized DALL-E prompts for AI/ML visualizations")
    image_descriptions: list = Field(..., description="Descriptions for each generated image")
    alt_text_suggestions: list = Field(..., description="Alt-text suggestions for accessibility")

class AIMLImageGenerator(BaseTool):
    name: str = "AI/ML Image Generator"
    description: str = "Generates optimized DALL-E prompts for AI/ML research visualizations including diagrams, infographics, and technical illustrations"
    
    def _run(self, topic: str, content_type: str, visualization_type: str) -> str:
        """
        Generate optimized DALL-E prompts for AI/ML research visualizations.
        """
        topic_lower = topic.lower()
        content_lower = content_type.lower()
        viz_lower = visualization_type.lower()
        
        # Base prompt templates for different AI/ML topics
        prompt_templates = {
            "llm": {
                "architecture": "Professional technical diagram of {topic} architecture, clean minimalist design, blue and white color scheme, showing neural network layers, transformers, attention mechanisms, vector embeddings, professional infographic style, high quality, detailed",
                "infographic": "Modern infographic about {topic}, clean design, professional color palette, showing key concepts, statistics, and insights, minimalist style, high quality, detailed",
                "flowchart": "Professional flowchart of {topic} process, clean lines, logical flow, blue and white color scheme, technical diagram style, high quality, detailed",
                "comparison": "Professional comparison chart of {topic}, side-by-side analysis, clean design, data visualization style, professional color scheme, high quality, detailed"
            },
            "rag": {
                "architecture": "Technical diagram of RAG (Retrieval-Augmented Generation) system architecture, showing knowledge base, retrieval system, language model, clean professional design, blue and green color scheme, high quality, detailed",
                "infographic": "Modern infographic explaining RAG systems, showing retrieval process, knowledge integration, response generation, clean design, professional colors, high quality, detailed",
                "flowchart": "Professional flowchart of RAG system workflow, showing query processing, document retrieval, knowledge synthesis, response generation, clean design, high quality, detailed",
                "comparison": "Comparison chart of different RAG approaches, showing performance metrics, accuracy comparisons, clean professional design, high quality, detailed"
            },
            "mlops": {
                "architecture": "Technical diagram of MLOps pipeline architecture, showing data processing, model training, deployment, monitoring, clean professional design, blue and orange color scheme, high quality, detailed",
                "infographic": "Modern infographic about MLOps best practices, showing automation, monitoring, deployment strategies, clean design, professional colors, high quality, detailed",
                "flowchart": "Professional flowchart of MLOps workflow, showing CI/CD pipeline, model versioning, deployment stages, clean design, high quality, detailed",
                "comparison": "Comparison chart of MLOps tools and platforms, showing features, capabilities, clean professional design, high quality, detailed"
            },
            "healthcare": {
                "architecture": "Technical diagram of healthcare AI system architecture, showing medical data processing, AI models, clinical decision support, clean professional design, medical blue color scheme, high quality, detailed",
                "infographic": "Modern infographic about healthcare AI applications, showing diagnosis, treatment, patient monitoring, clean design, professional medical colors, high quality, detailed",
                "flowchart": "Professional flowchart of healthcare AI workflow, showing data collection, analysis, clinical decision making, clean design, high quality, detailed",
                "comparison": "Comparison chart of healthcare AI approaches, showing accuracy, safety, regulatory compliance, clean professional design, high quality, detailed"
            },
            "general": {
                "architecture": "Professional technical diagram of {topic} system architecture, clean minimalist design, modern color scheme, showing components and connections, professional infographic style, high quality, detailed",
                "infographic": "Modern infographic about {topic}, clean design, professional color palette, showing key concepts and insights, minimalist style, high quality, detailed",
                "flowchart": "Professional flowchart of {topic} process, clean lines, logical flow, modern color scheme, technical diagram style, high quality, detailed",
                "comparison": "Professional comparison chart of {topic}, side-by-side analysis, clean design, data visualization style, professional color scheme, high quality, detailed"
            }
        }
        
        # Determine the appropriate template based on topic
        if "llm" in topic_lower or "large language model" in topic_lower:
            template_key = "llm"
        elif "rag" in topic_lower or "retrieval" in topic_lower:
            template_key = "rag"
        elif "mlops" in topic_lower or "production" in topic_lower:
            template_key = "mlops"
        elif "healthcare" in topic_lower or "clinical" in topic_lower:
            template_key = "healthcare"
        else:
            template_key = "general"
            
        # Generate prompts based on visualization type
        image_prompts = []
        image_descriptions = []
        alt_text_suggestions = []
        
        if "diagram" in viz_lower or "architecture" in viz_lower:
            prompt = prompt_templates[template_key]["architecture"].format(topic=topic)
            image_prompts.append(prompt)
            image_descriptions.append(f"Technical architecture diagram of {topic}")
            alt_text_suggestions.append(f"Technical diagram showing the architecture of {topic} system with components and data flow")
            
        if "infographic" in viz_lower or "info" in viz_lower:
            prompt = prompt_templates[template_key]["infographic"].format(topic=topic)
            image_prompts.append(prompt)
            image_descriptions.append(f"Infographic explaining {topic} concepts and insights")
            alt_text_suggestions.append(f"Infographic displaying key concepts and insights about {topic}")
            
        if "flowchart" in viz_lower or "process" in viz_lower:
            prompt = prompt_templates[template_key]["flowchart"].format(topic=topic)
            image_prompts.append(prompt)
            image_descriptions.append(f"Flowchart showing {topic} process and workflow")
            alt_text_suggestions.append(f"Flowchart illustrating the process and workflow of {topic}")
            
        if "comparison" in viz_lower or "chart" in viz_lower:
            prompt = prompt_templates[template_key]["comparison"].format(topic=topic)
            image_prompts.append(prompt)
            image_descriptions.append(f"Comparison chart of {topic} approaches and methods")
            alt_text_suggestions.append(f"Comparison chart showing different approaches and methods for {topic}")
            
        # Add a general visualization if no specific type matched
        if not image_prompts:
            prompt = prompt_templates[template_key]["infographic"].format(topic=topic)
            image_prompts.append(prompt)
            image_descriptions.append(f"Visual representation of {topic} concepts")
            alt_text_suggestions.append(f"Visual diagram illustrating key concepts of {topic}")
            
        # Add LinkedIn-specific optimizations
        if "linkedin" in content_lower:
            for i, prompt in enumerate(image_prompts):
                image_prompts[i] = prompt + ", optimized for social media, professional networking content"
                
        # Add blog-specific optimizations
        if "blog" in content_lower:
            for i, prompt in enumerate(image_prompts):
                image_prompts[i] = prompt + ", publication quality, academic research content"
                
        result = {
            "image_prompts": image_prompts,
            "image_descriptions": image_descriptions,
            "alt_text_suggestions": alt_text_suggestions,
            "topic": topic,
            "content_type": content_type,
            "visualization_type": visualization_type
        }
        
        return json.dumps(result, indent=2)

class ResearchPaperAnalyzerInput(BaseModel):
    paper_topic: str = Field(..., description="The research paper topic or title to analyze")
    research_area: str = Field(..., description="The research area or field")

class ResearchPaperAnalyzerOutput(BaseModel):
    research_significance: str = Field(..., description="Assessment of research significance")
    key_contributions: list = Field(..., description="Key contributions of the research")
    methodology_insights: list = Field(..., description="Methodology insights and innovations")
    practical_applications: list = Field(..., description="Practical applications and implications")
    publication_venues: list = Field(..., description="Suggested publication venues")

class ResearchPaperAnalyzer(BaseTool):
    name: str = "Research Paper Analyzer"
    description: str = "Analyzes research papers for significance, contributions, and insights for AI/ML research scientist content creation"
    
    def _run(self, paper_topic: str, research_area: str) -> str:
        """
        Analyze a research paper for significance, contributions, and insights.
        """
        # This tool would integrate with research databases in production
        # For now, providing structured guidance for research paper analysis
        
        topic_lower = paper_topic.lower()
        area_lower = research_area.lower()
        
        # Research significance assessment
        significance = "High"
        if any(word in topic_lower for word in ["novel", "breakthrough", "state-of-the-art", "sota"]):
            significance = "Very High"
        elif any(word in topic_lower for word in ["improvement", "enhancement", "optimization"]):
            significance = "High"
        elif any(word in topic_lower for word in ["comparison", "analysis", "study"]):
            significance = "Medium"
        else:
            significance = "Medium"
            
        # Key contributions based on research area
        contributions = []
        if "llm" in area_lower or "large language model" in area_lower:
            contributions = [
                "Novel architecture improvements",
                "Efficiency optimizations",
                "Performance enhancements",
                "Scalability improvements",
                "Interpretability advances"
            ]
        elif "rag" in area_lower or "retrieval" in area_lower:
            contributions = [
                "Advanced retrieval mechanisms",
                "Improved accuracy metrics",
                "Novel evaluation frameworks",
                "Multi-modal integration",
                "Real-time optimization"
            ]
        elif "mlops" in area_lower or "production" in area_lower:
            contributions = [
                "Automation improvements",
                "Monitoring enhancements",
                "Deployment optimizations",
                "Scalability solutions",
                "Cost reduction strategies"
            ]
        else:
            contributions = [
                "Novel methodology",
                "Performance improvements",
                "Efficiency gains",
                "Scalability enhancements",
                "Practical applications"
            ]
            
        # Methodology insights
        methodology_insights = [
            "Innovative approach to problem-solving",
            "Novel evaluation metrics",
            "Advanced optimization techniques",
            "Robust experimental design",
            "Comprehensive benchmarking"
        ]
        
        # Practical applications
        practical_applications = [
            "Industry deployment potential",
            "Real-world problem solving",
            "Commercial applications",
            "Research collaboration opportunities",
            "Technology transfer potential"
        ]
        
        # Publication venues
        publication_venues = []
        if "llm" in area_lower or "nlp" in area_lower:
            publication_venues = ["ACL", "EMNLP", "NAACL", "ICLR", "NeurIPS", "ICML"]
        elif "computer vision" in area_lower or "vision" in area_lower:
            publication_venues = ["CVPR", "ICCV", "ECCV", "ICLR", "NeurIPS", "ICML"]
        elif "reinforcement learning" in area_lower or "rl" in area_lower:
            publication_venues = ["ICLR", "NeurIPS", "ICML", "AAAI", "IJCAI"]
        else:
            publication_venues = ["ICLR", "NeurIPS", "ICML", "AAAI", "IJCAI", "KDD"]
            
        result = {
            "research_significance": significance,
            "key_contributions": contributions,
            "methodology_insights": methodology_insights,
            "practical_applications": practical_applications,
            "publication_venues": publication_venues,
            "paper_topic": paper_topic,
            "research_area": research_area
        }
        
        return json.dumps(result, indent=2)

class InnovationTrackerInput(BaseModel):
    topic: str = Field(..., description="The AI/ML topic to track for latest innovations")
    timeframe: str = Field(..., description="Timeframe for innovation tracking (e.g., 'last 3 months', 'last 6 months')")

class InnovationTrackerOutput(BaseModel):
    latest_innovations: list = Field(..., description="Latest innovations and developments")
    trending_topics: list = Field(..., description="Currently trending topics")
    emerging_technologies: list = Field(..., description="Emerging technologies to watch")
    industry_insights: list = Field(..., description="Key industry insights and trends")

class InnovationTracker(BaseTool):
    name: str = "AI/ML Innovation Tracker"
    description: str = "Tracks latest innovations, trends, and developments in AI/ML research for research scientist content creation"
    
    def _run(self, topic: str, timeframe: str) -> str:
        """
        Track latest innovations and trends in AI/ML research for content creation.
        """
        # This tool would integrate with real-time APIs in production
        # For now, providing structured guidance for innovation tracking
        
        topic_lower = topic.lower()
        
        # Latest innovations based on topic
        innovations = []
        trending_topics = []
        emerging_technologies = []
        industry_insights = []
        
        if "llm" in topic_lower or "large language model" in topic_lower:
            innovations = [
                "Multi-modal LLMs (GPT-4V, Claude 3 Vision)",
                "LLM reasoning improvements (Chain-of-Thought, Tree-of-Thoughts)",
                "Efficient fine-tuning techniques (QLoRA, DoRA)",
                "LLM safety and alignment research",
                "Open-source LLM developments (Llama 3, Mistral, Gemma)"
            ]
            trending_topics = [
                "LLM agents and autonomous systems",
                "RAG system optimizations",
                "LLM evaluation and benchmarking",
                "Cost optimization for LLM deployments"
            ]
            emerging_technologies = [
                "Retrieval-Augmented Generation (RAG) 2.0",
                "LLM orchestration frameworks",
                "Edge LLM deployment",
                "Federated learning for LLMs"
            ]
            
        elif "mlops" in topic_lower or "production ml" in topic_lower:
            innovations = [
                "MLOps automation and CI/CD for ML",
                "Model monitoring and observability",
                "Feature store implementations",
                "ML model versioning and governance",
                "ML pipeline orchestration tools"
            ]
            trending_topics = [
                "MLOps at scale",
                "Model drift detection and retraining",
                "ML security and privacy",
                "ML cost optimization"
            ]
            emerging_technologies = [
                "MLOps platforms (Weights & Biases, MLflow, Kubeflow)",
                "AutoML and automated feature engineering",
                "ML model compression and optimization",
                "ML model serving and inference optimization"
            ]
            
        elif "rag" in topic_lower or "retrieval augmented generation" in topic_lower:
            innovations = [
                "Advanced RAG architectures",
                "Multi-modal RAG systems",
                "RAG evaluation frameworks",
                "RAG optimization techniques",
                "RAG for enterprise applications"
            ]
            trending_topics = [
                "RAG system performance optimization",
                "RAG for real-time applications",
                "RAG security and privacy",
                "RAG integration with existing systems"
            ]
            emerging_technologies = [
                "Vector databases (Pinecone, Weaviate, Chroma)",
                "RAG orchestration frameworks",
                "Hybrid search and retrieval methods",
                "RAG for edge computing"
            ]
            
        elif "healthcare" in topic_lower or "clinical" in topic_lower:
            innovations = [
                "AI for medical imaging and diagnosis",
                "Clinical decision support systems",
                "Drug discovery and development",
                "Personalized medicine and genomics",
                "Healthcare data privacy and security"
            ]
            trending_topics = [
                "AI in telemedicine",
                "Clinical trial optimization",
                "Healthcare workflow automation",
                "AI for patient monitoring"
            ]
            emerging_technologies = [
                "Federated learning for healthcare",
                "AI-powered medical devices",
                "Healthcare-specific LLMs",
                "AI for drug repurposing"
            ]
            
        else:
            # General AI/ML innovations
            innovations = [
                "Foundation models and their applications",
                "AI safety and alignment research",
                "Multi-modal AI systems",
                "AI for scientific discovery",
                "Sustainable AI and green computing"
            ]
            trending_topics = [
                "AI regulation and governance",
                "AI ethics and responsible AI",
                "AI for climate change",
                "AI democratization and accessibility"
            ]
            emerging_technologies = [
                "Quantum machine learning",
                "Neuromorphic computing",
                "AI for edge devices",
                "Federated and distributed AI"
            ]
            
        industry_insights = [
            "Increased focus on AI safety and responsible development",
            "Growing demand for MLOps and production ML expertise",
            "Rise of AI-first companies and AI-native applications",
            "Convergence of AI with other emerging technologies",
            "Growing importance of AI governance and compliance"
        ]
        
        result = {
            "latest_innovations": innovations,
            "trending_topics": trending_topics,
            "emerging_technologies": emerging_technologies,
            "industry_insights": industry_insights,
            "tracking_timeframe": timeframe,
            "topic": topic
        }
        
        return json.dumps(result, indent=2)

class ResearchTopicAnalyzerInput(BaseModel):
    topic: str = Field(..., description="The research topic to analyze")
    field: str = Field(..., description="The field of research")

class ResearchTopicAnalyzerOutput(BaseModel):
    publication_potential: str = Field(..., description="Assessment of publication potential")
    target_journals: list = Field(..., description="Suggested target journals/platforms")
    research_gaps: list = Field(..., description="Identified research gaps")
    methodology_suggestions: list = Field(..., description="Suggested research methodologies")

class ResearchTopicAnalyzer(BaseTool):
    name: str = "Research Topic Analyzer"
    description: str = "Analyzes research topics for publication potential and provides suggestions for AI/ML research scientist content"
    
    def _run(self, topic: str, field: str) -> str:
        """
        Analyze a research topic for publication potential and provide suggestions for AI/ML research scientist content.
        """
        # This is a simplified analysis - in a real implementation, you might use
        # academic databases or research APIs for more accurate assessments
        
        # Basic publication potential assessment for AI/ML research scientist
        potential = "Medium"
        if any(word in topic.lower() for word in ["llm", "large language model", "rag", "retrieval augmented generation", "mlops", "production ml"]):
            potential = "High"
        elif any(word in topic.lower() for word in ["research", "novel", "breakthrough", "innovation"]):
            potential = "High"
        elif any(word in topic.lower() for word in ["ai", "machine learning", "deep learning", "neural networks"]):
            potential = "Medium"
        else:
            potential = "Low"
            
        # Suggested target journals/platforms for AI/ML research scientist
        journals = []
        if "llm" in field.lower() or "large language model" in field.lower():
            journals.extend(["arXiv", "ACL", "EMNLP", "ICLR", "NeurIPS", "ICML", "Medium", "Towards Data Science"])
        elif "mlops" in field.lower() or "production" in field.lower():
            journals.extend(["ICML", "KDD", "MLOps Community", "Towards Data Science", "Medium"])
        elif "research" in field.lower() or "academic" in field.lower():
            journals.extend(["ICLR", "NeurIPS", "ICML", "AAAI", "IJCAI", "arXiv"])
        elif "healthcare" in field.lower() or "clinical" in field.lower():
            journals.extend(["Nature Medicine", "JAMA", "Healthcare AI Blog", "Medium", "HealthTech Blogs"])
        elif "finance" in field.lower() or "fintech" in field.lower():
            journals.extend(["Quantitative Finance", "FinTech Blogs", "Medium", "TechCrunch"])
        else:
            journals.extend(["ICLR", "NeurIPS", "ICML", "arXiv", "Medium", "Towards Data Science"])
            
        # Research gaps and methodology suggestions for research scientist
        gaps = [
            "Limited research on optimal methods for production deployment",
            "Need for more comprehensive evaluation frameworks",
            "Gap in research on novel architectures",
            "Limited research on research methodology innovations"
        ]
        
        methodologies = [
            "Novel research methodology development",
            "Comprehensive experimental design",
            "Advanced evaluation frameworks",
            "Research innovation documentation"
        ]
        
        result = {
            "publication_potential": potential,
            "target_journals": journals,
            "research_gaps": gaps,
            "methodology_suggestions": methodologies
        }
        
        return json.dumps(result, indent=2)

class ResumeOptimizerInput(BaseModel):
    resume_content: str = Field(..., description="The resume content to optimize")
    target_role: str = Field(..., description="The target role/position")

class ResumeOptimizerOutput(BaseModel):
    optimization_suggestions: list = Field(..., description="Suggestions to optimize the resume")
    keyword_matches: list = Field(..., description="Keywords that match the target role")
    missing_keywords: list = Field(..., description="Keywords that should be added")
    overall_score: int = Field(..., description="Overall optimization score (1-10)")

class ResumeOptimizer(BaseTool):
    name: str = "Resume Optimizer"
    description: str = "Analyzes and optimizes resume content for AI/ML research scientist roles"
    
    def _run(self, resume_content: str, target_role: str) -> str:
        """
        Analyze and optimize resume content for AI/ML research scientist roles.
        """
        # This is a simplified analysis - in a real implementation, you might use
        # ATS systems or job description APIs for more accurate matching
        
        resume_lower = resume_content.lower()
        role_lower = target_role.lower()
        
        # Common keywords for AI/ML research scientist roles
        role_keywords = {
            "ai ml research scientist": ["research", "novel", "breakthrough", "innovation", "optimal methods", "publication", "academic", "scientist", "research", "analysis", "methodology"],
            "senior ai research scientist": ["research", "novel", "breakthrough", "innovation", "optimal methods", "publication", "academic", "scientist", "research", "analysis", "methodology", "senior", "lead", "mentor"],
            "ai research scientist": ["research", "novel", "breakthrough", "innovation", "optimal methods", "publication", "academic", "scientist", "research", "analysis", "methodology"],
            "ml research scientist": ["research", "novel", "breakthrough", "innovation", "optimal methods", "publication", "academic", "scientist", "research", "analysis", "methodology", "machine learning"],
            "research scientist": ["research", "novel", "breakthrough", "innovation", "optimal methods", "publication", "academic", "scientist", "research", "analysis", "methodology"]
        }
        
        # Find matching keywords
        matching_keywords = []
        missing_keywords = []
        
        for role, keywords in role_keywords.items():
            if role in role_lower:
                for keyword in keywords:
                    if keyword in resume_lower:
                        matching_keywords.append(keyword)
                    else:
                        missing_keywords.append(keyword)
                break
                
        # Optimization suggestions for research scientist roles
        suggestions = []
        if len(missing_keywords) > 0:
            suggestions.append(f"Add missing research scientist keywords: {', '.join(missing_keywords[:3])}")
        if len(resume_content.split()) < 300:
            suggestions.append("Expand on research responsibilities and scientific achievements")
        if "quantified" not in resume_lower and "metrics" not in resume_lower:
            suggestions.append("Add quantified research achievements and performance metrics")
        if "research" not in resume_lower and "scientist" not in resume_lower:
            suggestions.append("Emphasize research responsibilities and scientific expertise")
        if "publication" not in resume_lower and "paper" not in resume_lower:
            suggestions.append("Highlight research publications and papers")
        if "innovation" not in resume_lower and "novel" not in resume_lower:
            suggestions.append("Include research innovations and novel approaches")
            
        # Calculate overall score
        score = 5  # Base score
        score += len(matching_keywords) * 2
        score -= len(missing_keywords)
        score = max(1, min(10, score))
        
        result = {
            "optimization_suggestions": suggestions,
            "keyword_matches": matching_keywords,
            "missing_keywords": missing_keywords[:5],
            "overall_score": score
        }
        
        return json.dumps(result, indent=2)
