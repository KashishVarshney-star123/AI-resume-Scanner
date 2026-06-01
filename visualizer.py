import os
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend to prevent GUI thread issues in Flask
import matplotlib.pyplot as plt
from collections import Counter

def create_bar_chart(missing_skills):
    """Creates a horizontal bar chart of the top 5 missing skills and saves it as a PNG.
    
    Args:
        missing_skills (list or dict): A list of missing skill strings or a dictionary 
                                      mapping skill names to frequency counts.
                                      
    Returns:
        str: Relative path to the saved PNG image (e.g., 'static/charts/missing_skills.png').
    """
    # Ensure static/charts folder exists
    charts_dir = os.path.join('static', 'charts')
    os.makedirs(charts_dir, exist_ok=True)
    
    # Standardize input to extract top 5 skills with counts
    if isinstance(missing_skills, dict):
        sorted_skills = sorted(missing_skills.items(), key=lambda x: x[1], reverse=True)[:5]
    elif isinstance(missing_skills, list):
        counter = Counter(missing_skills)
        sorted_skills = counter.most_common(5)
    else:
        sorted_skills = []
        
    # Setup plot aesthetics
    fig, ax = plt.subplots(figsize=(8, 4.5))
    
    if not sorted_skills:
        # Graceful handling for empty state
        ax.text(0.5, 0.5, 'No Missing Skills Found', 
                horizontalalignment='center', verticalalignment='center',
                fontsize=14, color='#1a3a6b')
        ax.axis('off')
    else:
        # Reverse elements to display the highest value at the top of the horizontal bar chart
        sorted_skills.reverse()
        skills = [item[0] for item in sorted_skills]
        counts = [item[1] for item in sorted_skills]
        
        # Horizontal bar chart using dark blue theme (#1a3a6b)
        bars = ax.barh(skills, counts, color='#1a3a6b', edgecolor='none', height=0.55)
        
        # Hide top and right spines
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('#cccccc')
        ax.spines['bottom'].set_color('#cccccc')
        
        # Style tick markings and labels
        ax.tick_params(colors='#333333', labelsize=11)
        ax.set_xlabel('Frequency / Count', fontsize=12, color='#333333', labelpad=10)
        ax.set_title('Top Missing Skills', fontsize=14, fontweight='bold', color='#1a3a6b', pad=15)
        
        # Ensure x-axis ticks are integers if values are low
        max_count = max(counts) if counts else 0
        if max_count <= 10:
            ax.set_xticks(range(0, int(max_count) + 2))
            
        # Draw counts on each bar
        for bar in bars:
            width = bar.get_width()
            ax.text(width + (max_count * 0.02 or 0.1), bar.get_y() + bar.get_height() / 2, 
                    f'{int(width)}', va='center', ha='left', color='#333333', fontweight='semibold')
                    
    plt.tight_layout()
    
    # Save the plot
    file_path = os.path.join(charts_dir, 'missing_skills.png')
    plt.savefig(file_path, dpi=300, bbox_inches='tight')
    plt.close(fig)
    
    # Return formatted relative path for Flask endpoints
    return file_path.replace('\\', '/')
