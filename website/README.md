# Offline AI Chatbot Website

A modern, privacy-focused landing page for the Offline AI Chatbot application.

## Features

- Modern, premium design with dark theme
- Smooth animations and transitions
- Fully responsive (mobile, tablet, desktop)
- Optimized for performance
- Privacy-first messaging

## Deployment to Vercel

### Option 1: Deploy via Vercel CLI

1. Install Vercel CLI:
```bash
npm install -g vercel
```

2. Navigate to the website directory:
```bash
cd website
```

3. Deploy:
```bash
vercel
```

4. Follow the prompts to complete deployment

### Option 2: Deploy via Vercel Dashboard

1. Go to [vercel.com](https://vercel.com)
2. Sign in with GitHub, GitLab, or Bitbucket
3. Click "Add New Project"
4. Import your repository or upload the `website` folder
5. Vercel will automatically detect the configuration
6. Click "Deploy"

### Option 3: Deploy via GitHub

1. Push the `website` folder to a GitHub repository
2. Connect your GitHub account to Vercel
3. Import the repository
4. Vercel will auto-deploy on every push to main branch

## Important Note About Large Files

**The executable file (OfflineChatbot.exe) is ~57MB**, which may exceed Vercel's free tier limits for individual files.

### Solutions:

1. **Use GitHub Releases (Recommended)**:
   - Upload the .exe to GitHub Releases
   - Update the download link in `index.html` to point to the GitHub release URL
   - Example: `https://github.com/yourusername/repo/releases/download/v0.2.2/OfflineChatbot.exe`

2. **Use External Storage**:
   - Upload to Google Drive, Dropbox, or OneDrive
   - Get a direct download link
   - Update the href in the download button

3. **Use Vercel Blob Storage** (Paid):
   - Upload large files to Vercel Blob
   - Reference them in your site

## Local Development

To test the website locally:

1. Open `index.html` in a web browser, or
2. Use a local server:
```bash
# Python
python -m http.server 8000

# Node.js
npx serve
```

3. Visit `http://localhost:8000`

## File Structure

```
website/
├── index.html          # Main HTML file
├── styles.css          # Styling
├── script.js           # Interactive features
├── vercel.json         # Vercel configuration
├── dist/               # Executable files (update download link)
│   └── OfflineChatbot.exe
└── README.md           # This file
```

## Customization

- Update the download link in `index.html` (line with `href="dist/OfflineChatbot.exe"`)
- Modify colors in `styles.css` (CSS variables in `:root`)
- Add your own logo/images
- Update text content as needed

## License

Open source - free to use and modify.
