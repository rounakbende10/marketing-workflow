#!/usr/bin/env python3
"""
Metrics Dashboard for AI/ML Research Scientist System
Comprehensive dashboard for analyzing system performance, content quality, and business impact.
"""

import os
import json
from datetime import datetime
from metrics_analyzer import ResearchScientistMetricsAnalyzer
from mlflow_monitor import CrewAIMLflowMonitor

class ResearchScientistMetricsDashboard:
    """Dashboard for AI/ML Research Scientist metrics analysis"""
    
    def __init__(self):
        self.analyzer = ResearchScientistMetricsAnalyzer()
        self.monitor = CrewAIMLflowMonitor()
        
    def generate_comprehensive_report(self):
        """Generate a comprehensive metrics report"""
        
        print("📊 AI/ML Research Scientist Metrics Dashboard")
        print("=" * 60)
        print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        # Analyze current content
        content_metrics = self.analyzer.analyze_content_files()
        
        # Get MLflow experiment data
        experiment_summary = self.monitor.get_experiment_summary()
        
        # Generate comprehensive report
        self._print_executive_summary(content_metrics, experiment_summary)
        self._print_content_analysis(content_metrics)
        self._print_quality_metrics(content_metrics)
        self._print_business_impact_analysis(content_metrics)
        self._print_performance_metrics(content_metrics, experiment_summary)
        self._print_recommendations(content_metrics)
        
        # Save detailed report
        self._save_detailed_report(content_metrics, experiment_summary)
        
    def _print_executive_summary(self, content_metrics, experiment_summary):
        """Print executive summary"""
        print("🎯 EXECUTIVE SUMMARY")
        print("-" * 30)
        
        # Content generation summary
        linkedin_posts = content_metrics["content_generation"].get("linkedin_posts_generated", 0)
        research_blogs = content_metrics["content_generation"].get("research_blogs_generated", 0)
        visualizations = content_metrics["content_generation"].get("technical_visualizations_created", 0)
        
        print(f"📝 Content Generated:")
        print(f"   • LinkedIn Posts: {linkedin_posts}")
        print(f"   • Research Blogs: {research_blogs}")
        print(f"   • Technical Visualizations: {visualizations}")
        print(f"   • Total Content Pieces: {linkedin_posts + research_blogs + visualizations}")
        
        # Quality scores
        quality_score = content_metrics["quality_metrics"].get("technical_depth_score", 0)
        credibility_score = content_metrics["quality_metrics"].get("research_credibility_score", 0)
        business_impact = content_metrics["business_impact"].get("thought_leadership_potential", 0)
        
        print(f"\n📈 Quality Scores:")
        print(f"   • Technical Depth: {quality_score:.1%}")
        print(f"   • Research Credibility: {credibility_score:.1%}")
        print(f"   • Thought Leadership: {business_impact:.1%}")
        
        # Experiment summary
        if isinstance(experiment_summary, dict):
            total_runs = experiment_summary.get("total_runs", 0)
            print(f"\n🔬 Experiment Tracking:")
            print(f"   • Total Runs: {total_runs}")
            print(f"   • MLflow Server: Active")
        else:
            print(f"\n🔬 Experiment Tracking: {experiment_summary}")
        
        print()
        
    def _print_content_analysis(self, content_metrics):
        """Print detailed content analysis"""
        print("📋 CONTENT ANALYSIS")
        print("-" * 30)
        
        # LinkedIn Posts Analysis
        linkedin_data = content_metrics["content_generation"]
        print(f"🔗 LinkedIn Posts:")
        print(f"   • Generated: {linkedin_data.get('linkedin_posts_generated', 0)}")
        print(f"   • Total Words: {linkedin_data.get('linkedin_posts_total_words', 0):,}")
        print(f"   • Avg Length: {linkedin_data.get('linkedin_posts_avg_length', 0):.0f} words")
        print(f"   • With Hashtags: {linkedin_data.get('linkedin_posts_with_hashtags', 0)}")
        print(f"   • With Visualizations: {linkedin_data.get('linkedin_posts_with_visualizations', 0)}")
        print(f"   • Technical Depth: {linkedin_data.get('linkedin_posts_technical_depth', 0):.1%}")
        
        # Research Blogs Analysis
        blog_data = content_metrics["content_generation"]
        print(f"\n📚 Research Blogs:")
        print(f"   • Generated: {blog_data.get('research_blogs_generated', 0)}")
        print(f"   • Total Words: {blog_data.get('research_blogs_total_words', 0):,}")
        print(f"   • Avg Length: {blog_data.get('research_blogs_avg_length', 0):.0f} words")
        print(f"   • With Code: {blog_data.get('research_blogs_with_code', 0)}")
        print(f"   • With Diagrams: {blog_data.get('research_blogs_with_diagrams', 0)}")
        print(f"   • Technical Depth: {blog_data.get('research_blogs_technical_depth', 0):.1%}")
        
        # Visualizations Analysis
        viz_data = content_metrics["content_generation"]
        print(f"\n🎨 Technical Visualizations:")
        print(f"   • Total Created: {viz_data.get('technical_visualizations_created', 0)}")
        print(f"   • Architecture Diagrams: {viz_data.get('architecture_diagrams', 0)}")
        print(f"   • Performance Charts: {viz_data.get('performance_charts', 0)}")
        print(f"   • Comparison Infographics: {viz_data.get('comparison_infographics', 0)}")
        print(f"   • Implementation Flowcharts: {viz_data.get('implementation_flowcharts', 0)}")
        
        print()
        
    def _print_quality_metrics(self, content_metrics):
        """Print quality metrics analysis"""
        print("⭐ QUALITY METRICS")
        print("-" * 30)
        
        quality_data = content_metrics["quality_metrics"]
        
        print(f"🔬 Technical Depth Score: {quality_data.get('technical_depth_score', 0):.1%}")
        print(f"📚 Research Credibility Score: {quality_data.get('research_credibility_score', 0):.1%}")
        print(f"🚀 Innovation Tracking Score: {quality_data.get('innovation_tracking_score', 0):.1%}")
        print(f"🛠️ Practical Applicability Score: {quality_data.get('practical_applicability_score', 0):.1%}")
        print(f"✅ Content Completeness Score: {quality_data.get('content_completeness_score', 0):.1%}")
        
        # Quality assessment
        overall_quality = (quality_data.get('technical_depth_score', 0) + 
                          quality_data.get('research_credibility_score', 0)) / 2
        
        print(f"\n📊 Overall Quality Assessment:")
        if overall_quality >= 0.9:
            print(f"   🟢 EXCELLENT ({overall_quality:.1%}) - High-quality research content")
        elif overall_quality >= 0.8:
            print(f"   🟡 GOOD ({overall_quality:.1%}) - Solid technical content")
        elif overall_quality >= 0.7:
            print(f"   🟠 FAIR ({overall_quality:.1%}) - Adequate content quality")
        else:
            print(f"   🔴 NEEDS IMPROVEMENT ({overall_quality:.1%}) - Content quality below target")
        
        print()
        
    def _print_business_impact_analysis(self, content_metrics):
        """Print business impact analysis"""
        print("💼 BUSINESS IMPACT ANALYSIS")
        print("-" * 30)
        
        business_data = content_metrics["business_impact"]
        
        print(f"🎯 Target Audience Relevance: {business_data.get('target_audience_relevance', 0):.1%}")
        print(f"🧠 Thought Leadership Potential: {business_data.get('thought_leadership_potential', 0):.1%}")
        print(f"🤝 Networking Opportunity Score: {business_data.get('networking_opportunity_score', 0):.1%}")
        print(f"📈 Career Advancement Potential: {business_data.get('career_advancement_potential', 0):.1%}")
        
        # Business impact assessment
        overall_impact = (business_data.get('target_audience_relevance', 0) + 
                         business_data.get('thought_leadership_potential', 0)) / 2
        
        print(f"\n📊 Business Impact Assessment:")
        if overall_impact >= 0.9:
            print(f"   🟢 HIGH IMPACT ({overall_impact:.1%}) - Strong career advancement potential")
        elif overall_impact >= 0.8:
            print(f"   🟡 MODERATE IMPACT ({overall_impact:.1%}) - Good networking opportunities")
        elif overall_impact >= 0.7:
            print(f"   🟠 LIMITED IMPACT ({overall_impact:.1%}) - Some career benefits")
        else:
            print(f"   🔴 LOW IMPACT ({overall_impact:.1%}) - Needs improvement for career advancement")
        
        print()
        
    def _print_performance_metrics(self, content_metrics, experiment_summary):
        """Print performance metrics"""
        print("⚡ PERFORMANCE METRICS")
        print("-" * 30)
        
        # Research focus metrics
        research_data = content_metrics["research_focus"]
        print(f"🏗️ LLM Architecture Coverage: {research_data.get('llm_architecture_coverage', 0):.1%}")
        print(f"🚀 Performance Optimization Coverage: {research_data.get('performance_optimization_coverage', 0):.1%}")
        print(f"🔮 Emerging Technology Coverage: {research_data.get('emerging_technology_coverage', 0):.1%}")
        print(f"🛠️ Implementation Guidance Coverage: {research_data.get('implementation_guidance_coverage', 0):.1%}")
        
        # Engagement metrics
        engagement_data = content_metrics["engagement_metrics"]
        print(f"\n📱 Engagement Metrics:")
        print(f"   • Hashtag Optimization: {engagement_data.get('hashtag_optimization_score', 0):.1%}")
        print(f"   • Call-to-Action Effectiveness: {engagement_data.get('call_to_action_effectiveness', 0):.1%}")
        print(f"   • Content Shareability: {engagement_data.get('content_shareability_score', 0):.1%}")
        print(f"   • Professional Networking: {engagement_data.get('professional_networking_score', 0):.1%}")
        
        # Experiment performance
        if isinstance(experiment_summary, dict):
            print(f"\n🔬 Experiment Performance:")
            print(f"   • Total Runs: {experiment_summary.get('total_runs', 0)}")
            print(f"   • Latest Run: {experiment_summary.get('runs', [{}])[0].get('start_time', 'N/A') if experiment_summary.get('runs') else 'N/A'}")
        
        print()
        
    def _print_recommendations(self, content_metrics):
        """Print actionable recommendations"""
        print("💡 RECOMMENDATIONS")
        print("-" * 30)
        
        recommendations = []
        
        # Content volume recommendations
        linkedin_posts = content_metrics["content_generation"].get("linkedin_posts_generated", 0)
        research_blogs = content_metrics["content_generation"].get("research_blogs_generated", 0)
        visualizations = content_metrics["content_generation"].get("technical_visualizations_created", 0)
        
        if linkedin_posts < 5:
            recommendations.append("📝 Increase LinkedIn post generation to at least 5 posts for better networking")
        
        if research_blogs < 2:
            recommendations.append("📚 Generate at least 2 research blogs to demonstrate thought leadership")
        
        if visualizations < 3:
            recommendations.append("🎨 Create more technical visualizations to enhance content engagement")
        
        # Quality recommendations
        quality_data = content_metrics["quality_metrics"]
        if quality_data.get("technical_depth_score", 0) < 0.8:
            recommendations.append("🔬 Enhance technical depth by including more architectural analysis")
        
        if quality_data.get("research_credibility_score", 0) < 0.8:
            recommendations.append("📚 Add code examples and technical diagrams to improve credibility")
        
        # Business impact recommendations
        business_data = content_metrics["business_impact"]
        if business_data.get("thought_leadership_potential", 0) < 0.8:
            recommendations.append("🧠 Focus on creating more comprehensive research blogs for thought leadership")
        
        if business_data.get("networking_opportunity_score", 0) < 0.8:
            recommendations.append("🤝 Increase LinkedIn post frequency and engagement strategies")
        
        # Engagement recommendations
        engagement_data = content_metrics["engagement_metrics"]
        if engagement_data.get("hashtag_optimization_score", 0) < 0.7:
            recommendations.append("🏷️ Improve hashtag usage in LinkedIn posts for better discoverability")
        
        if engagement_data.get("content_shareability_score", 0) < 0.7:
            recommendations.append("📤 Add more visual content and infographics to increase shareability")
        
        # Print recommendations
        if recommendations:
            for i, rec in enumerate(recommendations, 1):
                print(f"{i}. {rec}")
        else:
            print("✅ All metrics are within target ranges. Great job!")
        
        print()
        
    def _save_detailed_report(self, content_metrics, experiment_summary):
        """Save detailed report to file"""
        report_data = {
            "timestamp": datetime.now().isoformat(),
            "content_metrics": content_metrics,
            "experiment_summary": experiment_summary,
            "dashboard_version": "1.0"
        }
        
        report_file = "metrics_dashboard_report.json"
        with open(report_file, 'w') as f:
            json.dump(report_data, f, indent=2)
        
        print(f"📄 Detailed report saved to: {report_file}")
        print("🌐 View MLflow experiments at: http://localhost:5001")
        print()

def main():
    """Main function to run the metrics dashboard"""
    dashboard = ResearchScientistMetricsDashboard()
    dashboard.generate_comprehensive_report()

if __name__ == "__main__":
    main()
