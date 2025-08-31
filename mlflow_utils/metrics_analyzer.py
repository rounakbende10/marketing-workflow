#!/usr/bin/env python3
"""
Metrics Analyzer for AI/ML Research Scientist System
Comprehensive metrics calculation and analysis for content quality, technical depth, and business impact.
"""

import os
import re
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any
import mlflow

class ResearchScientistMetricsAnalyzer:
    """Analyzes metrics for AI/ML Research Scientist content generation"""
    
    def __init__(self):
        self.metrics = {}
        
    def analyze_content_files(self, base_path: str = ".") -> Dict[str, Any]:
        """Analyze generated content files and calculate comprehensive metrics"""
        
        metrics = {
            "content_generation": {},
            "technical_analysis": {},
            "quality_metrics": {},
            "business_impact": {},
            "performance_metrics": {},
            "research_focus": {},
            "engagement_metrics": {}
        }
        
        # Analyze LinkedIn posts
        linkedin_posts = self._analyze_linkedin_posts(base_path)
        metrics["content_generation"].update(linkedin_posts)
        
        # Analyze research blogs
        research_blogs = self._analyze_research_blogs(base_path)
        metrics["content_generation"].update(research_blogs)
        
        # Analyze technical visualizations
        visualizations = self._analyze_visualizations(base_path)
        metrics["content_generation"].update(visualizations)
        
        # Calculate technical depth and quality metrics
        quality_metrics = self._calculate_quality_metrics(metrics["content_generation"])
        metrics["quality_metrics"].update(quality_metrics)
        
        # Calculate business impact metrics
        business_metrics = self._calculate_business_impact_metrics(metrics["content_generation"])
        metrics["business_impact"].update(business_metrics)
        
        # Calculate research focus metrics
        research_metrics = self._calculate_research_focus_metrics(metrics["content_generation"])
        metrics["research_focus"].update(research_metrics)
        
        # Calculate engagement metrics
        engagement_metrics = self._calculate_engagement_metrics(metrics["content_generation"])
        metrics["engagement_metrics"].update(engagement_metrics)
        
        return metrics
    
    def _analyze_linkedin_posts(self, base_path: str) -> Dict[str, Any]:
        """Analyze LinkedIn posts for metrics"""
        metrics = {
            "linkedin_posts_generated": 0,
            "linkedin_posts_total_words": 0,
            "linkedin_posts_avg_length": 0,
            "linkedin_posts_with_hashtags": 0,
            "linkedin_posts_with_visualizations": 0,
            "linkedin_posts_technical_depth": 0.0
        }
        
        # Check for LinkedIn posts file
        linkedin_file = os.path.join(base_path, "research_linkedin_posts.md")
        if os.path.exists(linkedin_file):
            with open(linkedin_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Count posts (assuming each post is separated by --- or similar)
            posts = re.split(r'---+\n', content)
            metrics["linkedin_posts_generated"] = len([p for p in posts if p.strip()])
            
            # Calculate word count
            total_words = len(content.split())
            metrics["linkedin_posts_total_words"] = total_words
            metrics["linkedin_posts_avg_length"] = total_words / max(metrics["linkedin_posts_generated"], 1)
            
            # Count posts with hashtags
            hashtag_posts = len(re.findall(r'#\w+', content))
            metrics["linkedin_posts_with_hashtags"] = hashtag_posts
            
            # Check for visualizations
            viz_posts = len(re.findall(r'!\[.*?\]\(.*?\)', content))
            metrics["linkedin_posts_with_visualizations"] = viz_posts
            
            # Calculate technical depth
            technical_terms = len(re.findall(r'\b(LLM|transformer|architecture|performance|benchmark|optimization|implementation|algorithm|model|training|inference)\b', content, re.IGNORECASE))
            metrics["linkedin_posts_technical_depth"] = min(1.0, technical_terms / max(total_words, 1) * 100)
        
        return metrics
    
    def _analyze_research_blogs(self, base_path: str) -> Dict[str, Any]:
        """Analyze research blogs for metrics"""
        metrics = {
            "research_blogs_generated": 0,
            "research_blogs_total_words": 0,
            "research_blogs_avg_length": 0,
            "research_blogs_with_code": 0,
            "research_blogs_with_diagrams": 0,
            "research_blogs_technical_depth": 0.0
        }
        
        # Check for research blogs file
        blogs_file = os.path.join(base_path, "research_blogs.md")
        if os.path.exists(blogs_file):
            with open(blogs_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Count blogs (assuming each blog is separated by --- or similar)
            blogs = re.split(r'---+\n', content)
            metrics["research_blogs_generated"] = len([b for b in blogs if b.strip()])
            
            # Calculate word count
            total_words = len(content.split())
            metrics["research_blogs_total_words"] = total_words
            metrics["research_blogs_avg_length"] = total_words / max(metrics["research_blogs_generated"], 1)
            
            # Count blogs with code blocks
            code_blocks = len(re.findall(r'```[\w]*\n.*?\n```', content, re.DOTALL))
            metrics["research_blogs_with_code"] = code_blocks
            
            # Count blogs with diagrams
            diagrams = len(re.findall(r'!\[.*?\]\(.*?\)', content))
            metrics["research_blogs_with_diagrams"] = diagrams
            
            # Calculate technical depth
            technical_terms = len(re.findall(r'\b(architecture|performance|benchmark|optimization|implementation|algorithm|model|training|inference|efficiency|scalability|latency|throughput)\b', content, re.IGNORECASE))
            metrics["research_blogs_technical_depth"] = min(1.0, technical_terms / max(total_words, 1) * 100)
        
        return metrics
    
    def _analyze_visualizations(self, base_path: str) -> Dict[str, Any]:
        """Analyze technical visualizations for metrics"""
        metrics = {
            "technical_visualizations_created": 0,
            "architecture_diagrams": 0,
            "performance_charts": 0,
            "comparison_infographics": 0,
            "implementation_flowcharts": 0
        }
        
        # Visualization analysis removed to reduce token usage
        # Focus on content-based metrics instead
        
        return metrics
    
    def _calculate_quality_metrics(self, content_metrics: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate quality metrics based on content analysis"""
        metrics = {
            "technical_depth_score": 0.0,
            "research_credibility_score": 0.0,
            "innovation_tracking_score": 0.0,
            "practical_applicability_score": 0.0,
            "content_completeness_score": 0.0
        }
        
        # Calculate technical depth score
        linkedin_depth = content_metrics.get("linkedin_posts_technical_depth", 0)
        blog_depth = content_metrics.get("research_blogs_technical_depth", 0)
        metrics["technical_depth_score"] = (linkedin_depth + blog_depth) / 2 / 100
        
        # Calculate research credibility score
        blogs_generated = content_metrics.get("research_blogs_generated", 0)
        blogs_with_code = content_metrics.get("research_blogs_with_code", 0)
        blogs_with_diagrams = content_metrics.get("research_blogs_with_diagrams", 0)
        
        credibility_factors = []
        if blogs_generated > 0:
            credibility_factors.append(0.4)  # Base credibility for having blogs
            if blogs_with_code > 0:
                credibility_factors.append(0.4)  # Code examples add credibility
            if blogs_with_diagrams > 0:
                credibility_factors.append(0.2)  # Diagrams add credibility
        
        metrics["research_credibility_score"] = sum(credibility_factors) if credibility_factors else 0.0
        
        # Calculate innovation tracking score
        total_content = content_metrics.get("linkedin_posts_generated", 0) + content_metrics.get("research_blogs_generated", 0)
        metrics["innovation_tracking_score"] = min(1.0, total_content / 10)  # Scale based on content volume
        
        # Calculate practical applicability score
        if blogs_with_code > 0:
            metrics["practical_applicability_score"] = 0.8
        else:
            metrics["practical_applicability_score"] = 0.5
        
        # Calculate content completeness score
        completeness_factors = []
        if content_metrics.get("linkedin_posts_generated", 0) >= 5:
            completeness_factors.append(0.4)
        if content_metrics.get("research_blogs_generated", 0) >= 2:
            completeness_factors.append(0.4)
        if content_metrics.get("linkedin_posts_with_hashtags", 0) > 0:
            completeness_factors.append(0.1)
        if content_metrics.get("research_blogs_with_diagrams", 0) > 0:
            completeness_factors.append(0.1)
        
        metrics["content_completeness_score"] = sum(completeness_factors)
        
        return metrics
    
    def _calculate_business_impact_metrics(self, content_metrics: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate business impact metrics"""
        metrics = {
            "target_audience_relevance": 0.0,
            "thought_leadership_potential": 0.0,
            "networking_opportunity_score": 0.0,
            "career_advancement_potential": 0.0
        }
        
        # Target audience relevance
        total_posts = content_metrics.get("linkedin_posts_generated", 0)
        total_blogs = content_metrics.get("research_blogs_generated", 0)
        total_content = total_posts + total_blogs
        
        if total_content >= 10:
            metrics["target_audience_relevance"] = 0.95
        elif total_content >= 5:
            metrics["target_audience_relevance"] = 0.85
        elif total_content >= 2:
            metrics["target_audience_relevance"] = 0.75
        else:
            metrics["target_audience_relevance"] = 0.5
        
        # Thought leadership potential
        if content_metrics.get("research_blogs_generated", 0) >= 2:
            metrics["thought_leadership_potential"] = 0.95
        elif content_metrics.get("research_blogs_generated", 0) >= 1:
            metrics["thought_leadership_potential"] = 0.85
        else:
            metrics["thought_leadership_potential"] = 0.7
        
        # Networking opportunity score
        if content_metrics.get("linkedin_posts_generated", 0) >= 5:
            metrics["networking_opportunity_score"] = 0.9
        elif content_metrics.get("linkedin_posts_generated", 0) >= 2:
            metrics["networking_opportunity_score"] = 0.8
        else:
            metrics["networking_opportunity_score"] = 0.6
        
        # Career advancement potential
        career_factors = []
        if content_metrics.get("research_blogs_generated", 0) > 0:
            career_factors.append(0.5)
        if content_metrics.get("linkedin_posts_generated", 0) >= 3:
            career_factors.append(0.5)
        
        metrics["career_advancement_potential"] = sum(career_factors)
        
        return metrics
    
    def _calculate_research_focus_metrics(self, content_metrics: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate research focus metrics"""
        metrics = {
            "llm_architecture_coverage": 0.0,
            "performance_optimization_coverage": 0.0,
            "emerging_technology_coverage": 0.0,
            "implementation_guidance_coverage": 0.0
        }
        
        # LLM architecture coverage
        if content_metrics.get("research_blogs_generated", 0) > 0:
            metrics["llm_architecture_coverage"] = 0.95
        else:
            metrics["llm_architecture_coverage"] = 0.7
        
        # Performance optimization coverage
        if content_metrics.get("research_blogs_generated", 0) > 0:
            metrics["performance_optimization_coverage"] = 0.9
        else:
            metrics["performance_optimization_coverage"] = 0.6
        
        # Emerging technology coverage
        total_content = content_metrics.get("linkedin_posts_generated", 0) + content_metrics.get("research_blogs_generated", 0)
        if total_content >= 5:
            metrics["emerging_technology_coverage"] = 0.85
        elif total_content >= 2:
            metrics["emerging_technology_coverage"] = 0.75
        else:
            metrics["emerging_technology_coverage"] = 0.6
        
        # Implementation guidance coverage
        if content_metrics.get("research_blogs_with_code", 0) > 0:
            metrics["implementation_guidance_coverage"] = 0.8
        else:
            metrics["implementation_guidance_coverage"] = 0.6
        
        return metrics
    
    def _calculate_engagement_metrics(self, content_metrics: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate engagement metrics"""
        metrics = {
            "hashtag_optimization_score": 0.0,
            "call_to_action_effectiveness": 0.0,
            "content_shareability_score": 0.0,
            "professional_networking_score": 0.0
        }
        
        # Hashtag optimization score
        posts_with_hashtags = content_metrics.get("linkedin_posts_with_hashtags", 0)
        total_posts = content_metrics.get("linkedin_posts_generated", 0)
        
        if total_posts > 0:
            hashtag_ratio = posts_with_hashtags / total_posts
            metrics["hashtag_optimization_score"] = min(1.0, hashtag_ratio * 1.2)
        else:
            metrics["hashtag_optimization_score"] = 0.0
        
        # Call to action effectiveness
        if content_metrics.get("linkedin_posts_generated", 0) >= 3:
            metrics["call_to_action_effectiveness"] = 0.8
        elif content_metrics.get("linkedin_posts_generated", 0) >= 1:
            metrics["call_to_action_effectiveness"] = 0.7
        else:
            metrics["call_to_action_effectiveness"] = 0.5
        
        # Content shareability score
        if content_metrics.get("research_blogs_generated", 0) > 0:
            metrics["content_shareability_score"] = 0.85
        else:
            metrics["content_shareability_score"] = 0.6
        
        # Professional networking score
        networking_factors = []
        if content_metrics.get("linkedin_posts_generated", 0) >= 5:
            networking_factors.append(0.5)
        elif content_metrics.get("linkedin_posts_generated", 0) >= 2:
            networking_factors.append(0.4)
        
        if content_metrics.get("research_blogs_generated", 0) > 0:
            networking_factors.append(0.5)
        
        metrics["professional_networking_score"] = min(1.0, sum(networking_factors))
        
        return metrics
    
    def log_metrics_to_mlflow(self, metrics: Dict[str, Any]):
        """Log all calculated metrics to MLflow"""
        
        # Flatten metrics for MLflow logging
        flat_metrics = {}
        
        for category, category_metrics in metrics.items():
            for metric_name, value in category_metrics.items():
                flat_metrics[f"{category}_{metric_name}"] = value
        
        # Log all metrics
        for metric_name, value in flat_metrics.items():
            if isinstance(value, (int, float)):
                mlflow.log_metric(metric_name, value)
        
        # Log summary metrics
        mlflow.log_metric("overall_content_quality_score", 
                         (metrics["quality_metrics"]["technical_depth_score"] + 
                          metrics["quality_metrics"]["research_credibility_score"]) / 2)
        
        mlflow.log_metric("overall_business_impact_score",
                         (metrics["business_impact"]["target_audience_relevance"] + 
                          metrics["business_impact"]["thought_leadership_potential"]) / 2)
        
        mlflow.log_metric("overall_engagement_score",
                         (metrics["engagement_metrics"]["hashtag_optimization_score"] + 
                          metrics["engagement_metrics"]["content_shareability_score"]) / 2)

def main():
    """Main function to demonstrate metrics analysis"""
    analyzer = ResearchScientistMetricsAnalyzer()
    metrics = analyzer.analyze_content_files()
    
    print("📊 AI/ML Research Scientist Metrics Analysis")
    print("=" * 50)
    
    for category, category_metrics in metrics.items():
        print(f"\n🔍 {category.replace('_', ' ').title()}:")
        for metric_name, value in category_metrics.items():
            print(f"  {metric_name}: {value}")
    
    # Log to MLflow if available
    try:
        analyzer.log_metrics_to_mlflow(metrics)
        print("\n✅ Metrics logged to MLflow successfully!")
    except Exception as e:
        print(f"\n⚠️ Could not log to MLflow: {e}")

if __name__ == "__main__":
    main()
