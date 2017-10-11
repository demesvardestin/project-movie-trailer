import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>TrailFlix - Browse Your Favorite Trailers</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link href="https://fonts.googleapis.com/css?family=Maven+Pro" rel="stylesheet">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            background: #f5fcf9;
            font-family: 'Maven Pro', sans-serif;
        }
        html, body {
            overflow-x: hidden;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            padding-bottom: 20px;
        }
        .movie-tile:hover {
            
        }
        .movie-image:hover {
            filter: brightness(40%);
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .navbar {
            background: #2FC2EF;
            height: auto;
            box-shadow: 0px 5px 10px gray;
        }
        .container-body {
            padding-left: 160px;
            padding-right: 160px;
            padding-top: 50px;
        }
        .movie-div{
            margin-bottom: 20px;
            padding: 0;
        }
        .movie-image{
            height: 400px;
            width: 290px;
            border: 1px solid #a3e1cc;
            border-radius: 4px;
        }
        .navbar-brand{
            font-family: 'Maven Pro', sans-serif;
            color: #fff;
            font-size: 34px;
        }
        .btn {
            font-size: 22px;
        }
        .links {
            font-size: 25px;
            color: #fff;
        }
        .trailer-button {
            padding-left: 8.5px;
            padding-right: 8.5px;
        }
        .navbar-right {
            padding-right: 40px;
        }
        links:hover {
            color: #2FC2EF;
        }
        footer {
            background: #97e0f7;
            height: auto;
        }
        .footer-container {
            padding-left: 25px;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.trailer-button', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-fixed-top" role="navigation">
        <div class="navbar-header">
            <a class="navbar-brand" href="#">TrailFlix</a>
        </div>
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            <ul class="nav navbar-nav navbar-right">
                <li><a href="#" class="links" data-toggle="dropdown">Action</a></li>
                <li><a href="#" class="links">Comedy</a></li>
                <li><a href="#" class="links">Documentary</a></li>
                <li><a href="#" class="links">Sports</a></li>
            </ul>
        </div>
      </div>
    </div>
    <div class="container-body">
        <div class="row">
          {movie_tiles}
        </div>
    </div>
    <footer>
        <div class="footer-container">
            <div class="row">
                <div class="col-md-4 text-left">
                    <h4>&copy; Demesvar Destin</h4>
                </div>
            </div>
        </div>
    </footer>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
    <div class="col-md-3 movie-tile">
        <!-- Movie details modal **I have been unable to individualize the modal. For some reason, using {movie_id} as data-target/id does not work** -->
        <div class="modal fade" id="details" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h3 class="modal-title" id="myModalLabel">Movie Details</h3>
              </div>
              <div class="modal-body">
                <h4>
                    <strong>Title</strong>: {movie_title} </br >
                    <strong>Description</strong>: {movie_description} <br />
                    <strong>Genre</strong>: {movie_genre} <br />
                    <strong>Release Date</strong>: {movie_release} <br />
                    <strong>Notable Actors</strong>: {movie_actors} <br />
                    <strong>Box Office</strong>: {movie_box_office} <br />
                </h4>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
              </div>
            </div>
          </div>
        </div>
        <div class="movie-div">
            <img src="{poster_image_url}" class="movie-image">
        </div>
        <div class="movie-name">
            <h2>{movie_title}</h2>
        </div>
        <div class="button-actions">
            <!-- <a data-toggle="modal" data-target="#details" class="btn btn-primary btn-lg">Details</a> -->
            <button class="btn btn-info btn-lg trailer-button" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">Play Trailer</button>
            <button class="btn btn-primary btn-lg trailer-button" data-toggle="modal" data-target="#details">Movie Details</button>
        </div>
    </div>
'''
        
    
def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title = movie.title,
            movie_id = movie.movie_id,
            poster_image_url = movie.poster_image_url,
            trailer_youtube_id = trailer_youtube_id,
            movie_description = movie.description,
            movie_genre = movie.genre,
            movie_release = movie.release,
            movie_box_office = movie.box_office,
            movie_actors = movie.actors
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
