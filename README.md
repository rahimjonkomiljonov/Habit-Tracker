# Pixela Reading Tracker

A Python script that interacts with the Pixela API to track daily reading habits in pages.

## Features
- Creates a Pixela user account
- Sets up a reading graph
- Adds daily reading data (pixels)
- Updates existing pixel data
- Deletes pixel data
- Uses current date automatically

## Prerequisites
- Python 3.x
- Required Python packages:
  - `requests`
- Pixela account credentials:
  - Username
  - Token

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/pixela-reading-tracker.git
cd pixela-reading-tracker
```

2. Install dependencies:
```bash
pip install requests
```

## Configuration
- `USERNAME`: Default "rahimjon"
- `TOKEN`: Your Pixela API token
- `GRAPH_ID`: Default "graph0012"
- Graph settings:
  - Name: "Reading graph"
  - Unit: "pages"
  - Type: "int"
  - Color: "shibafu" (green)

## Usage
1. Update the script with your Pixela credentials:
   - Replace `USERNAME` and `TOKEN`
2. Uncomment desired API calls:
   - User creation
   - Graph creation
   - Pixel posting
   - Pixel updating
   - Pixel deletion
3. Run the script:
```bash
python pixela_tracker.py
```

## How It Works
- **User Creation**: POST to create a new Pixela user
- **Graph Setup**: POST to create a reading graph
- **Add Pixel**: POST to add daily reading data
- **Update Pixel**: PUT to modify existing data
- **Delete Pixel**: DELETE to remove data
- Uses current date in YYYYMMDD format

## API Endpoints
- User: `https://pixe.la/v1/users`
- Graph: `/users/{username}/graphs`
- Pixel: `/users/{username}/graphs/{graph_id}`
- Update/Delete: `/users/{username}/graphs/{graph_id}/{date}`

## Code Structure
- Constants defined at top
- Separate endpoint configurations
- Reusable headers with token
- Commented-out example calls
- Current implementation: Delete pixel

## Customization
- Change `USERNAME`, `TOKEN`, and `GRAPH_ID`
- Modify `graph_config`:
  - `id`, `name`, `unit`, `type`, `color`
- Update `update_pixel_params["quantity"]`
- Uncomment and modify `pixel_params` for input

## Notes
- Most API calls are commented out - enable as needed
- Uses "shibafu" (green) color for graph
- Token passed via `X-USER-TOKEN` header
- Date format: YYYYMMDD
- Example update sets 120 pages

## Requirements.txt
```
requests
```

## Limitations
- Single graph support
- No error handling beyond basic requests
- Manual credential management
- One operation at a time (due to commented code)

## License
[MIT License](LICENSE)

## Disclaimer
- Replace default credentials before use
- Pixela API rate limits apply
- For personal use - secure your token
- Uncomment only one operation at a time to avoid conflicts
```

