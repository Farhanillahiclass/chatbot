from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from whatsapp_app.auth import login_required
from whatsapp_app.models import KeywordRule, db

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/")
@login_required
def index():
    rules = KeywordRule.query.filter_by(user_id=session["user_id"]).all()
    return render_template("dashboard.html", rules=rules)


@dashboard_bp.route("/rules/add", methods=["POST"])
@login_required
def add_rule():
    keyword = request.form.get("keyword", "").strip()
    reply = request.form.get("reply", "").strip()

    if not keyword or not reply:
        flash("Both keyword and reply are required.", "error")
        return redirect(url_for("dashboard.index"))

    rule = KeywordRule(
        keyword=keyword,
        reply=reply,
        user_id=session["user_id"],
    )
    db.session.add(rule)
    db.session.commit()
    flash("Rule added successfully.", "success")
    return redirect(url_for("dashboard.index"))


@dashboard_bp.route("/rules/delete/<int:rule_id>", methods=["POST"])
@login_required
def delete_rule(rule_id: int):
    rule = KeywordRule.query.get_or_404(rule_id)
    if rule.user_id != session["user_id"]:
        flash("Unauthorized.", "error")
        return redirect(url_for("dashboard.index"))

    db.session.delete(rule)
    db.session.commit()
    flash("Rule deleted.", "success")
    return redirect(url_for("dashboard.index"))
