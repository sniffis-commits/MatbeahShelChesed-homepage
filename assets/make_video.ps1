# Builds a short silent instructional MP4 from the REAL application screenshots.
# Requires ffmpeg on PATH. No AI-generated imagery is used.
$ErrorActionPreference = 'Stop'
$assets = Split-Path -Parent $MyInvocation.MyCommand.Path
$screens = Join-Path $assets 'screens'
$cards = Join-Path $assets 'cards'
$out = Join-Path $assets 'instructional.mp4'

$images = @(
  (Join-Path $cards '00-intro.png'),
  (Join-Path $screens '01-landing-en.png'),
  (Join-Path $cards '02-add-coins.png'),
  (Join-Path $screens '03-charity-box.png'),
  (Join-Path $cards '04-choose.png'),
  (Join-Path $screens '04-donate.png'),
  (Join-Path $screens '02-dashboard.png'),
  (Join-Path $cards '06-verify.png'),
  (Join-Path $screens '05-history.png'),
  (Join-Path $cards '09-kiosk.png'),
  (Join-Path $screens '07-kiosk-en.png'),
  (Join-Path $cards '10-outro.png')
)

$duration = 2.5
$transition = 0.5
$ffmpegArgs = @('-y', '-hide_banner', '-loglevel', 'error')
foreach ($image in $images) {
  $ffmpegArgs += @('-loop', '1', '-t', "$duration", '-i', $image)
}

$filters = @()
for ($i = 0; $i -lt $images.Count; $i++) {
  $filters += "[$($i):v]fps=24,scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2:color=0x0c2a1e,setsar=1,format=yuv420p[v$i]"
}
$last = 'v0'
for ($i = 1; $i -lt $images.Count; $i++) {
  $offset = ($duration - $transition) * $i
  $offsetText = $offset.ToString('0.0', [Globalization.CultureInfo]::InvariantCulture)
  $chain = "x$i"
  $filters += "[$last][v$i]xfade=transition=fade:duration=$($transition.ToString('0.0',[Globalization.CultureInfo]::InvariantCulture)):offset=$offsetText[$chain]"
  $last = $chain
}
$filters += "[$last]null[final]"

$ffmpegArgs += @(
  '-filter_complex', ($filters -join ';'),
  '-map', '[final]',
  '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '27',
  '-pix_fmt', 'yuv420p', '-movflags', '+faststart', '-an', $out
)
& ffmpeg @ffmpegArgs
if ($LASTEXITCODE -ne 0) { throw "ffmpeg failed with exit code $LASTEXITCODE" }
Get-Item $out | Select-Object Name, Length
