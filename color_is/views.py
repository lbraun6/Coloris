from django.shortcuts import render, redirect
import random

# Create your views here.


def game_view(request):
    # Initialize or get the score from the session
    score = request.session.get("score", 0)
    final_score = request.session.get("final_score", 0)

    # Logic to get a random color
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)

    # Set the current color in the session
    request.session['current_color'] = [red, green, blue]

    # Get round number
    round_number = request.session.get('round_number', 1)

    context = {
        "score": score,
        "current_color": (red, green, blue),
        "round_number": round_number,
        "final_score": final_score
    }
    request.session.save()

    return render(request, 'game_template.html', context)


def evaluate_guess_view(request):
    if request.method == 'POST':
        # Get individual RGB components from the form data
        red = int(request.POST.get('red', 0))
        green = int(request.POST.get('green', 0))
        blue = int(request.POST.get('blue', 0))

        # Get the current color from the session if it exists
        current_color = request.session.get("current_color", [0, 0, 0])
        current_round = request.session.get('round_number', 1)
        current_score = request.session.get('score', 0)

        if current_round >= 5:
            # Start a new round
            new_round = 1
            new_score = 0

            # Update the session with the new score and round number
            request.session['score'] = new_score
            request.session['round_number'] = new_round

            final_score = current_score + 100
            final_score -= round((abs(red - current_color[0]) / 765) * 100, 0)
            final_score -= round((abs(blue - current_color[1]) / 765) * 100, 0)
            final_score -= round((abs(green - current_color[2]) / 765) * 100, 0)

            request.session["final_score"] = final_score

            return redirect("color_is:final_score_view")
        else:
            # Logic to evaluate the user's guess and update the score
            new_score = current_score + 100
            new_score -= round((abs(red - current_color[0]) / 765) * 100, 0)
            new_score -= round((abs(blue - current_color[1]) / 765) * 100, 0)
            new_score -= round((abs(green - current_color[2]) / 765) * 100, 0)

            # Increment round number
            new_round = current_round + 1

        # Update the session with the new score and round number
        request.session['score'] = new_score
        request.session['round_number'] = new_round
        request.session["final_score"] = 0

    # Redirect to the next round or display the results
    request.session.save()
    return redirect('color_is:game_view')


def final_score_view(request):
    # Initialize or get the score from the session
    final_score = request.session.get("final_score", 0)

    context = {
        "final_score": final_score
    }
    request.session.save()

    return render(request, 'final_score_template.html', context)

