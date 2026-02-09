from flask import Flask, render_template

app = Flask(__name__)

# --- GLOBAL DATA ---
project_data = [
    {
        "id": "social-media",
        "title": "Social Media",
        "desc": "Promotional flyer campaigns and Instagram graphics.",
        "img": "lsu.jpg",
        "year": "2025",
        "role": "Graphic Designer",
        "content": "A deep dive into the visual strategy used for campus recruitment. This campaign focused on bold typography and high-contrast visuals to capture student attention across social media platforms.",
        
        # --- NEW: CATEGORIZED GALLERIES ---
        "galleries": [
            {
                "title": "Himalayas Chapter - Lambda Sigma Upsilon Latino Fraternity, Inc.",
                "images": ["social1.jpg", "social2.jpg", "social3.jpg", "social4.jpg", "social5.jpg", "social6.jpg", "social7.jpg", "social8.jpg", "social9.jpg", "social10.jpg", "social11.jpg", "social12.jpg"] 
            },
            {
                "title": "Regional Board Work",
                # Make sure to add these files to your images folder later!
                # You can use 'lsu.jpg' as a placeholder for now if you don't have them yet.
                "images": ["region1.jpg", "region2.jpg", "region3.jpg", "region4.jpg", "region5.jpg", "region6.jpg", "region7.jpg", "region8.jpg", "region9.jpg", "region10.jpg", "region11.jpg", "region12.jpg", "region13.jpg", "region14.jpg", "region15.jpg", "region16.jpg", "region17.jpg", "region18.jpg", "region19.jpg", "region20.jpg", "region21.jpg", "region22.jpg", "region23.jpg", "region24.jpg"] 
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html', projects=project_data)

@app.route('/project/<project_id>')
def project_detail(project_id):
    project = next((p for p in project_data if p['id'] == project_id), None)
    
    if project:
        return render_template('project_detail.html', project=project)
    else:
        return "Project not found", 404
    
# --- NEW: RESUME ROUTE ---
@app.route('/resume')
def resume():
    return render_template('resume.html')

# --- NEW: ABOUT PAGE ROUTE ---
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)